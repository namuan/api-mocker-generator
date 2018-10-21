from slugify import slugify

from .schema_generator import generate_schema


class Response:
    path: str
    method: str
    description: str
    http_status_code: int
    response_mock_file: str = None
    response_mock_content: str = None

    def __init__(self, path, method, response_code, response_spec):
        self.path = path
        self.method = method
        self.http_status_code = response_code
        self.description = response_spec['description']
        if response_spec.get('schema'):
            self.response_mock_content = generate_schema(response_spec['schema'])
            self.response_mock_file = self.slug()

    def slug(self):
        return slugify(f"{self.path}-{self.method}-{self.http_status_code}") + ".json"

    def __str__(self):
        return f"{self.http_status_code}"


class PathMethod:
    http_method: str
    responses: list

    def __init__(self, path, method, method_spec):
        self.http_method = method
        self.responses = [Response(path, method, k, v) for k, v in method_spec['responses'].items()]

    def __str__(self):
        return self.http_method


class Path:
    path: str
    just_methods: list
    methods: list

    def __init__(self, path, path_specs):
        self.path = path
        self.just_methods = [m for m in path_specs.keys()]
        self.methods = [PathMethod(path, k, v) for k, v in path_specs.items()]

    def __str__(self):
        return f"Path: {self.path} and methods: {self.methods}"


def extract_path_info(http_path, http_path_specs) -> Path:
    return Path(
        path=http_path,
        path_specs=http_path_specs
    )
