# term-weaver
Materialize LinkML enumerations



## Install
For using on a local machine, it is recommended to add the dev dependencies: 

```bash
pip install -e ".[dev]" 
```

This enables rich output which can be helpful.

## Running the script
`tweaver -s {path/to/source/files} -m {model_name}`

- The tool uses the model name to create the output filepath as `src/{model_name}/schema`


## Model YAML File Conventions
The tool copies the source model YAML file to make the expanded model YAML file.
The file is written to the output filepath location and uses the path to create the name.

Example:<br>
- output = src/enums_expanded_file<br>
- expanded model YAML = src/enums_expanded_file/enums_expanded_file.yaml

The tool uses text substituion to modify the content of the "id", "name", "title", and "description" properties. All instances of the word `source` are replaced with `expanded` in these fields.

The following conventions must be used for files to be findable by the script:
- The source model YAML file must include `_source` in the title<br>
  - Example: enums_source_file
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
