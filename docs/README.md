# term-weaver
Materialize LinkML enumerations



## Install
For using on a local machine, it is recommended to add the dev dependencies: 

```bash
pip install -e ".[dev]" 
```

This enables rich output which can be helpful.

## Running the script
`tweaver -s {path/to/source/files} -o {path/to/output/directory}`

## Model File Conventions
The tool copies the source model YAML file to make the expanded model YAML file.
The file is written to the output filepath location and uses the path to create the name.
&emsp;Example:   
&emsp;output = src/enums_expanded_file
&emsp;expanded model YAML = src/enums_expanded_file/enums_expanded_file.yaml

The tool uses text substituion to modify the content of the "id", "name", "title", and "description" properties. All instances of the word `source` are replaced with `expanded` in these fields.

The following convention must be used in the source model YAML file to be findable by the script:
- The file must include `_source` in the title
&emsp;- Example: enums_source_file

## [LinkML properties](https://linkml.io/linkml-model/latest/docs/ReachabilityQuery/) currently supported
- source_ontology 
- source_nodes
- relationship_types 
  - only supporting rdfs:subClassOf
- is_direct
- include_self
