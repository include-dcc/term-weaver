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

## [LinkML properties](https://linkml.io/linkml-model/latest/docs/ReachabilityQuery/) currently supported
- source_ontology 
- source_nodes
- relationship_types 
  - only supporting rdfs:subClassOf
- is_direct
- include_self
