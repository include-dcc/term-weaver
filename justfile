expand:
    -tweaver -s src/cam_source_enums/schema/ -m cam_expanded_enums

mini:
    -mini -s src/cam_source_enums/schema/

clear file_path:
    mini --clear {{file_path}}
