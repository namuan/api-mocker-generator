import os
from pathlib import Path

from jinja2 import Template

file_path = os.path.dirname(os.path.realpath(__file__))

config_json_file = Path(file_path + "/templates/config.json.j2").read_text()
config_json_template = Template(config_json_file)


def render_config_template(**params) -> str:
    return config_json_template.render(**params)
