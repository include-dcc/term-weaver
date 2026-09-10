expand:
    -weaver -s src/cam_source_enums/schema/

clear file_path:
    weaver --clear src/cam_source_enums/schema/{{file_path}}.yaml

handle url output action="":
    owl_handle -u {{url}} -o {{output}} {{if action == "" { "" } else { "-a " + action } }}
