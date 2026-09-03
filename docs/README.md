# term-weaver
Materialize LinkML enumerations



## Install
For using on a local machine, it is recommended to add the dev dependencies: 

```bash
pip install -e ".[dev]" 
```

This enables rich output which can be helpful.

## Running the script
### To write the expanded output inline:
`weaver -s {path/to/source/directory}` or `just expand`

Example:

`weaver -s src/cam_source_enums/schema/`

#### Re-expansion
To rerun the expansion script on a file, remove the `permissible_values` field from the YAML file. This can either be done by deleting it manually or running the following script for each file:

`weaver --clear {file_name}` or `just clear {file_name}`

Example:

`weaver --clear EnumName` or `just clear EnumName`

#### Working with OWL files

- OWL files in OWL2 Functional-Style Syntax (FFS) will need to be converted to RDF/XML to parse the descendants. 

To convert the OWL file, run the following command:

`just handle {OWL_url} {path/to/output/file}`

Example:

`just handle http://ontology.org/ffs.owl ontology/ffs.owl`

- OWL files too large to open from the URL will need to first be saved to a file directory inside the project and added to OWL_LOCAL_FILES in src/tweaver/weaver.py

To save the OWL file, run the following command:

`just handle {OWL_url} {path/to/output/file} save`

Example:

`just handle http://ontology.org/large.owl ontology/large.owl save`

To use the OWL file to expand the enumerations, add the OWL URL and path to output to **src/tweaver/weaver.py**:

```
OWL_LOCAL_FILES = {
    "http://ontology.org/large.owll": Path("ontology/large.owl")
}
```

## Model YAML File Conventions
The following conventions must be used for files to be findable by the script:
- The enumeration file names must start with `Enum`<br>
  - Example: EnumDataFile

## Prefixes
The ontology prefixes used in the expanded enumeration files are consistent with prefixes supported by LinkML.
- snomedct:
    - OLS is used to materialize enumerations and returns the prefix as "SNOMED"
    - The "SNOMED" value is replaced by the standard "snomedct"
- Other prefixes default to using the casing of the prefix provided in the file's `source_nodes`

## [LinkML properties](https://linkml.io/linkml-model/latest/docs/ReachabilityQuery/) currently supported
- source_ontology 
- source_nodes
- relationship_types 
  - only supporting rdfs:subClassOf
- is_direct
- include_self
