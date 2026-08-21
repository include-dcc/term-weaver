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

`weaver --clear EnumName`


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
