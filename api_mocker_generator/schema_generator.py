from .json_generator import *


def generate_schema(response_schema):
    schema_type = response_schema['type']
    if schema_type == 'array':
        return fuzz_array(response_schema)
    elif schema_type == 'object' and response_schema.get('properties'):
        return fuzz_object(response_schema['properties'])
