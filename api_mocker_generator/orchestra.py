import json

from .data_model import *
from .output_generator import write_output
from .swagger_doc import retrieve_swagger_doc
from .template_renderer import render_config_template


def play(swagger_doc: str, output_dir: str) -> None:
    swagger_spec = retrieve_swagger_doc(swagger_doc)
    base_path = swagger_spec.specification["basePath"]
    swagger_paths = swagger_spec.specification['paths']

    paths = [
        extract_path_info(path, path_specs)
        for path, path_specs in swagger_paths.items()
    ]

    rendered_config = render_config_template(
        base_path=base_path,
        paths=paths
    )

    write_output(output_dir + "/config.json", rendered_config)

    mock_files = [
        (r.response_mock_file, r.response_mock_content)
        for p in paths
        for m in p.methods
        for r in m.responses if r.response_mock_content
    ]

    for file_name, file_content in mock_files:
        write_output(output_dir + "/" + file_name, json.dumps(file_content, sort_keys=True, indent=4))
