# Enumeration Expansion - Allowable Prefixes

When we expand codes from ontologies like OBI where they import codes from other
ontologies as part of the ontogogy itself, there will need to be acknowledgement
on the part of the modeler to accept or deny those codes as appropriate for the
expansion.

For the time being, Term Weaver will simply abort when it runs into an
unexpected prefix, informing the modeler what it requested and what it
encountered with the expectation that the modeler will make the necessary
changes to their enumerations before trying to expand.

## LinkML Annotations

LinkML annotations should be added to each enumeration's reachable_from where
these are encountered indicating which prefixes are allowable and which are to
simply be ignored. An example might look like the following:

```yaml
---
id: https://includedcc.org/common-access-model/EnumAssayType
name: EnumAssayType
enums:
  EnumAssayType:
    description: Type of assays performed
    is_a: EnumNull
    reachable_from:
      source_ontology: bioregistry:obi
      source_nodes:
        - obi:0000070
      include_self: true
      is_direct: false
      relationship_types:
        - rdfs:subClassOf
      annotations:
        allowable_prefix:
          - CHMO
        ignore_prefix:
          - xkcd
```

When term-weaver is rerun with the annotations above, it will recognize CHMO as
valid, but will happily ignore those pesky [xkcd](https://xkcd.com/927/) terms
without halting.

## Important Note - Updating Model Prefixes

By forcing the modeler to acknowledge the unexpected prefix and fixing it, we
provide the opportunity for the modeler to correctly update their prefix list
and add any necessary prefixes. It should be noted that, as of this time, that
is solely up to the modeler to manage and will not result in an error if they
fail to do.
