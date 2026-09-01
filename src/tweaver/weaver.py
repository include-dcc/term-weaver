import argparse
import csv
import io
import logging
import re
import subprocess
import urllib.request
from pathlib import Path

import pyhornedowl
import yaml
from car_utils import setup_logging
from rdflib import OWL, RDF, RDFS, Graph, URIRef
from rdflib.namespace import SKOS

from tweaver.__init__ import __version__

logger = logging.getLogger(__name__)
# Rich Logging if rich is installed


prefix_dict = {"SNOMED": "snomedct", "SNOMEDCT": "snomedct", "SNOMEDCT_US": "snomedct"}
OWL_LOCAL_FILES = {
    "http://purl.org/ga4gh/kin.owl": Path("converted/kin.owl"),
    "http://purl.obolibrary.org/obo/ncit.owl": Path("converted/ncit.owl"),
}


def parsed_csv(csv_text: str, endpoint: str, source_nodes: list) -> dict:
    """Parse dragon_search CSV output into permissible_values object for enum yaml file."""
    reader = csv.DictReader(io.StringIO(csv_text))
    permissible_values = {}
    argument = "children" if endpoint == "-c" else "descendants"
    for row in reader:
        code = row["descendant_code"]
        for key, value in prefix_dict.items():
            code = code.replace(key, value)
        if code.lower() == "no results":
            print(f"No {argument} found for {row['parent_code']}")
            continue
        for node in source_nodes:
            split_code = code.split(":")[0].upper()
            split_node = node.split(":")[0].upper()
            if split_code != split_node:
                logger.warning(f"{code} prefix does not match the source node: {node}")
            if split_code == split_node:
                code = code.replace(code.split(":")[0], node.split(":")[0])
        permissible_values[code] = {
            "title": row.get("display", ""),
            "description": row.get("description"),
            "meaning": code,
        }
        if not permissible_values[code]["description"]:
            del permissible_values[code]["description"]
    return permissible_values


class IndentedDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow=flow, indentless=False)


def _resolve_enum_imports(imports: list, local_filepath: Path) -> list[Path]:
    """Resolve enum imports list to file path."""
    resolved = []
    for imp in imports:
        if not imp.split("/")[-1].startswith("Enum"):
            continue
        filename = imp.split("/")[-1]
        matches = list(local_filepath.resolve().glob(f"**/{filename}.yaml"))
        if not matches:
            logger.warning(f"{imp} file not found.")
            continue
        resolved.append(matches[0])
    return resolved


def _parse_reachable(reachable: dict) -> dict:
    """Parse reachable_from block."""
    source_ontology = reachable.get("source_ontology")
    return {
        "ontology": source_ontology.split(":")[1]
        if source_ontology and ":" in source_ontology
        else None,
        "nodes": reachable.get("source_nodes"),
        "is_direct": reachable.get("is_direct"),
        "include_self": reachable.get("include_self"),
        "minus": reachable.get("minus"),
    }


def _compute_minus_codes(
    reachable: dict, endpoint: str, iri: str | None, enum_file: Path, has_nodes: list
) -> set:
    """Compute the set of codes to exclude from permissible_values."""
    minus = reachable.get("minus", [])
    minus_codes = set()
    if isinstance(minus, dict):
        minus_codes.update(minus.get("permissible_values", []))
    else:
        for minus_item in minus:
            if isinstance(minus_item, str):
                minus_codes.add(minus_item)
                continue
            if "permissible_values" in minus_item:
                minus_codes.update(minus_item["permissible_values"])
                continue
            parsed = _parse_reachable(minus_item.get("reachable_from", {}))
            if not parsed["nodes"] or not parsed["ontology"]:
                continue
            for node in parsed["nodes"]:
                minus_codes.add(node)
                node_values, failed = _expand_enum_for_node(
                    node,
                    parsed["ontology"],
                    enum_file,
                    endpoint,
                    parsed,
                    has_nodes,
                    iri,
                )
                if not failed:
                    minus_codes.update(node_values.keys())
    return minus_codes


def _expand_enum_for_node(
    node: str,
    ontology: str,
    expanded_enum: Path,
    endpoint: str,
    reachable: dict,
    has_nodes: list,
    iri: str | None,
):
    """Run dragon_search for a single node and return parsed permissible values"""
    cmd = [
        "dragon_search",
        "-ak",
        str(node),
        "-o",
        str(ontology),
        "-f",
        str(expanded_enum),
        str(endpoint),
        "-s",
        "0",
    ]
    if reachable.get("include_self"):
        cmd.append("-p")
    if iri:
        cmd.extend(["-i", str(iri)])

    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        logger.error(f"Failed for {node}: {result.stdout}")
        logger.error(f"Failed for {node}: {result.stderr}")
        return {}, True
    parsed_nodes = parsed_csv(expanded_enum.read_text(), endpoint, has_nodes)
    return parsed_nodes, False


def _write_expanded_enum(
    expanded_enum: Path, parsed: dict, name: str, permissible_values: dict
):
    """Write the expanded enum YAML file with permissible_values."""
    parsed["enums"][name]["permissible_values"] = permissible_values
    expanded_enum.write_text(
        yaml.dump(
            parsed,
            Dumper=IndentedDumper,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
            explicit_start=True,
        )
    )


def _iri_to_curie(iri: str, source_prefix: str) -> str:
    """Convert a full IRI to a CURIE."""
    # OBO style: http://purl.obolibrary.org/obo/NCIT_C90528
    if "/obo/" in iri:
        local = iri.split("/obo/")[-1]  # NCIT_C90528
        return local.replace("_", ":", 1)  # NCIT:C90528
    # Hash style: http://purl.org/ga4gh/kin.owl#KIN_001
    if "#" in iri:
        local = iri.split("#")[-1]  # KIN_001
        prefix = local.split("_")[0]  # KIN
        return f"{prefix}:{local}"  # KIN:KIN_001
    return iri


def _curie_to_iri(curie: str, onto) -> str | None:
    return onto.get_iri_for_id(curie)


def get_owl_descendants(
    filepath: Path,
    source_nodes: list,
    ontology_url: str,
    is_direct: bool = False,
    include_self: bool = False,
) -> dict:
    logger.info(f"OWL source_nodes: {source_nodes}")
    onto = pyhornedowl.open_ontology(str(filepath))
    onto.build_indexes()
    permissible_values = {}
    logger.info(f"get_iri_for_id: {onto.get_iri_for_id}")
    for node in source_nodes:
        node_uri = onto.get_iri_for_id(node)
        if not node_uri:
            prefix, local = node.split(":", 1)

            for iri in onto.get_all_iris():
                if str(iri).rsplit("#", 1)[-1] == local:
                    node_uri = iri
                    break
        if not node_uri:
            logger.warning(f"Could not resolve {node} to a URI")
            continue

        logger.info(f"{node} -> {node_uri}")
        onto = pyhornedowl.open_ontology(str(filepath))
        onto.build_indexes()
        logger.info(
            f"ONTO METHODS: {[x for x in dir(onto) if 'iri' in x.lower() or 'id' in x.lower()]}"
        )
        if include_self:
            label = onto.get_annotation(
                node_uri, "http://www.w3.org/2000/01/rdf-schema#label"
            )
            entry = {"title": label or node}
            entry["meaning"] = node
            permissible_values[node] = entry

        descendants = (
            onto.get_subclasses(node_uri)
            if is_direct
            else onto.get_descendants(node_uri)
        )
        for desc_uri in descendants:
            curie = _iri_to_curie(desc_uri, node.split(":", 1)[0]) or desc_uri
            label = onto.get_annotation(
                desc_uri, "http://www.w3.org/2000/01/rdf-schema#label"
            )
            description = onto.get_annotation(
                desc_uri, "http://www.w3.org/2004/02/skos/core#definition"
            )
            entry = {"title": label or curie}
            if description:
                entry["description"] = description
            entry["meaning"] = curie
            permissible_values[curie] = entry

    return permissible_values


def _expand_owl(
    ontology_url: str,
    source_nodes: list,
    is_direct: bool,
    include_self: bool,
) -> dict:
    """Expand enum permissible values from an OWL file using rdflib."""

    g = Graph()

    local_file = OWL_LOCAL_FILES.get(ontology_url)
    owl_definition = URIRef(
        "http://www.geneontology.org/formats/oboInOwl#hasDefinition"
    )
    iao_definition = URIRef("http://purl.obolibrary.org/obo/IAO_0000115")
    if local_file and local_file.exists():
        g.parse(str(local_file))
        logger.info(f"Using local converted file: {local_file}")
        # return get_owl_descendants(
        # local_file, source_nodes, ontology_url, is_direct, include_self
        # )
        # for node in source_nodes:
        #     prefix = node.split(":")[0]
        #     g.bind(prefix, f"{ontology_url}#")
    else:
        logger.info(f"Loading OWL file from {ontology_url}")
        g.parse(ontology_url)

    def get_label(uri):
        for label in g.objects(URIRef(uri), RDFS.label):
            return str(label)
        return None

    def get_description(uri):
        for predicate in (
            SKOS.definition,
            owl_definition,
            iao_definition,
        ):
            for desc in g.objects(URIRef(uri), predicate):
                return str(desc)

        return None

    def get_descendants(node_uri, direct_only, predicate=None):
        if predicate is None:
            node_types = {str(obj) for obj in g.objects(URIRef(node_uri), RDF.type)}

            if str(OWL.ObjectProperty) in node_types:
                predicate = RDFS.subPropertyOf
            else:
                predicate = RDFS.subClassOf

        descendants = set()

        for s, _, _ in g.triples((None, predicate, URIRef(node_uri))):
            child_uri = str(s)
            descendants.add(child_uri)

            if not direct_only:
                descendants.update(get_descendants(child_uri, direct_only, predicate))

        return descendants

    def uri_to_curie(uri, source_prefix, source_ontology):
        output_prefix = prefix_dict.get(
            source_prefix.upper(),
            source_prefix,
        )

        uri = str(uri)

        # OBO IRIs: NCIT_C90528 -> NCIT:C90528
        if "/obo/" in uri:
            local = uri.rsplit("/obo/", 1)[1]
            return local.replace("_", ":", 1)

        # Fragment-based ontologies: KIN_003 -> KIN:KIN_003
        if "#" in uri:
            local = uri.rsplit("#", 1)[1]
            return f"{output_prefix}:{local}"

        # Path-based ontologies: topic_0610 -> edam:topic_0610
        ontology_namespace = source_ontology.rsplit("/", 1)[0] + "/"
        if uri.startswith(ontology_namespace):
            local = uri[len(ontology_namespace) :]
            return f"{output_prefix}:{local}"

        return uri

    permissible_values = {}
    for node in source_nodes:
        prefix, local = node.split(":", 1)

        node_uri = None

        for subject in g.subjects():
            subject_str = str(subject)

            # OBO: NCIT:C90528 -> NCIT_C90528
            if "/obo/" in subject_str:
                obo_id = subject_str.rsplit("/obo/", 1)[1]
                if obo_id == f"{prefix}_{local}":
                    node_uri = subject
                    break

            # Fragment-based: KIN:KIN_001 -> ...#KIN_001
            elif "#" in subject_str:
                if subject_str.rsplit("#", 1)[1] == local:
                    node_uri = subject
                    break

            # Path-based: edam:topic_0003 -> .../topic_0003
            elif subject_str.rsplit("/", 1)[-1] == local:
                node_uri = subject
                break

        if not node_uri:
            logger.warning(f"Could not resolve {node} to a URI")
            continue

        logger.info(f"{node} -> {node_uri}")

        if include_self:
            label = get_label(node_uri)
            desc = get_description(node_uri)
            entry = {"title": label or node}
            if desc:
                entry["description"] = desc
            entry["meaning"] = node
            permissible_values[node] = entry

        descendants = get_descendants(node_uri, is_direct)
        for desc_uri in descendants:
            curie = uri_to_curie(desc_uri, node.split(":")[0], ontology_url)
            label = get_label(desc_uri)
            description = get_description(desc_uri)
            entry = {"title": label or curie}
            if description:
                entry["description"] = description
            entry["meaning"] = curie
            permissible_values[curie] = entry

    return permissible_values


def expand(
    local_filepath: Path,
    iri: str | None = None,
):
    """Extract Enums from a monolithic LinkML model into individual YAML files
    Args:
        local_filepath: The file cont aining the monolithic linkml model
        iri: Optional iri if a specific iri is desired other than the iri derived programattically
    Returns:
        list of enum names
    """

    model_filename = local_filepath.parent.name + ".yaml"
    model_file = local_filepath / model_filename

    expanded_count = 0
    enum_names = []
    if not model_file.exists():
        logger.error(f"{model_file} not found.")
        return enum_names

    model_parsed = yaml.safe_load(model_file.read_text())
    imports = model_parsed.get("imports", [])
    enum_files = _resolve_enum_imports(imports, local_filepath)

    for enum_file in enum_files:
        raw_enum = enum_file.read_text()
        parsed = yaml.safe_load(raw_enum)
        enums = parsed.get("enums", {})

        for name, enum in enums.items():
            enum_names.append(name)
            reachable = _parse_reachable(enum.get("reachable_from") or {})
            endpoint = "-c" if reachable["is_direct"] else "-d"
            has_permissible = (
                "permissible_values" in enum and enum["permissible_values"]
            )
            has_ontology = (enum.get("reachable_from") or {}).get("source_ontology")
            if has_permissible or not reachable["ontology"] or not has_ontology:
                logger.info(f"Skipping {name}. Does not require expansion.")
                expanded_count += 1
                continue

            if not reachable["nodes"]:
                continue

            minus_codes = _compute_minus_codes(
                enum.get("reachable_from") or {},
                endpoint,
                iri,
                enum_file,
                reachable["nodes"],
            )
            all_permissible_values = {}
            node_failed = False
            logger.info(f"Expanding {name}: {has_ontology}")
            if has_ontology and ".owl" in has_ontology:
                all_permissible_values = _expand_owl(
                    ontology_url=has_ontology,
                    source_nodes=reachable["nodes"],
                    is_direct=reachable["is_direct"] or False,
                    include_self=reachable["include_self"] or False,
                )
                if all_permissible_values:
                    logger.info(
                        f"{name}: OWL expansion returned "
                        f"{len(all_permissible_values)} values"
                    )
                else:
                    node_failed = True
                    logger.warning(f"{name}: OWL expansion returned no values")
            else:
                for node in reachable["nodes"]:
                    node_values, failed = _expand_enum_for_node(
                        node,
                        reachable["ontology"],
                        enum_file,
                        endpoint,
                        reachable,
                        reachable["nodes"],
                        iri,
                    )

                    if failed:
                        node_failed = True
                        logger.warning(f"{node}: Search Dragon expansion failed")
                    else:
                        all_permissible_values.update(node_values)
                        logger.info(f"Expanded enumeration: {name}")

            if minus_codes:
                logger.info(f"Excluding {minus_codes}")
                all_permissible_values = {
                    k: v
                    for k, v in all_permissible_values.items()
                    if k not in minus_codes
                }

            if all_permissible_values:
                _write_expanded_enum(enum_file, parsed, name, all_permissible_values)
                if not node_failed:
                    expanded_count += 1

    enum_count = len(enum_names)
    if expanded_count != enum_count:
        logger.warning(f"{enum_count - expanded_count} failed to be expanded.")
    return enum_names


def restricted_chars(arg: str):
    allowed_chars = re.search(r"^[\w-]+$", arg)
    if not allowed_chars:
        parser.error(
            f"Invalid input '{arg}'. Model names can only contain alphanumeric characters, underscores, and dashes. See LinkML docs for more details: https://linkml.io/linkml/schemas/models.html#model-level-metadata-and-directives"
        )
    return arg


def clear_permissible_values(filepath: Path):
    """Remove the permissible_values block from an enum YAML file.
    Args:
        filepath: The filepath to the file to remove permissible_values
    """
    if not filepath.exists():
        logger.error(f"{filepath} not found.")
        return
    parsed = yaml.safe_load(filepath.read_text())
    enums = parsed.get("enums", {})
    for name in enums:
        if "permissible_values" in enums[name] and "reachable_from" in enums[name]:
            del enums[name]["permissible_values"]
            logger.info(f"Cleared permissible_values from {name}")
        elif "permissible_values" not in enums[name]:
            logger.warning(
                f"Cannot delete permissible_values in {name}. 'permissible_values' not present."
            )
        elif "reachable_from" not in enums[name]:
            logger.warning(
                f"Cannot delete permissible_values in {name}. 'reachable_from' not present."
            )
    filepath.write_text(
        yaml.dump(
            parsed,
            Dumper=IndentedDumper,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
            explicit_start=True,
        )
    )


parser = argparse.ArgumentParser(
    description="Expand enums from a monolithic LinkML model"
)


def exec(cli_args: list[str] | None = None):

    parser.add_argument(
        "-log",
        "--log-level",
        choices=["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Logging level tolerated (default is INFO)",
    )
    parser.add_argument(
        "-s",
        "--source",
        required=False,
        type=Path,
        help="The source file containing the enumerations to be expanded",
    )

    parser.add_argument(
        "-i",
        "--iri",
        required=False,
        default=None,
        help="Optional iri for the parent code to pull descendants.",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"{__version__}",
        help="Pulls the version from the __init__.py file",
    )
    parser.add_argument(
        "--clear",
        required=False,
        type=Path,
        help="Clears permissible_values property from a speficied enum YAML file.",
    )

    args = parser.parse_args(cli_args)
    setup_logging(level=args.log_level)
    if args.clear:
        clear_permissible_values(args.clear)
        return

    if not args.source:
        parser.error("-s/--source is required when not using --clear")
    expand(
        local_filepath=args.source,
        iri=args.iri,
    )
    return
