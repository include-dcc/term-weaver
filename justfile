expand:
    -weaver -s src/cam_source_enums/schema/

clear file_path:
    weaver --clear src/cam_source_enums/schema/{{file_path}}.yaml

convert url output:
    owl_convert -u {{url}} -o {{output}}
