import json
import jsonschema
from os.path import join, dirname
from jsonschema import validate
import jsonref


def assert_valid_schema(data, schemafile):
    """Checks whether the given data matches the schema"""

    schema = _load_json_schema(schemafile)
    return validate(data, schema)


def _load_json_schema(filename):
    """ Loads the given schema file"""

    relative_path = join("schemas", filename)
    absolute_path = join(dirname(__file__), relative_path)

    base_path = dirname(absolute_path)
    base_uri = 'file://{}/'.format(base_path)

    print(f"base uri {base_uri}")
    print(f"base path {base_path}")
    print(f"relative_path {relative_path}")
    print(f"absolute_path {absolute_path}")

    with open(absolute_path) as schema_file:
        return jsonref.loads(schema_file.read(), base_uri=base_uri, jsonschema=True)

def _load_json_data(filename):
    """ Loads the given schema file"""

    relative_path = join("data", filename)
    absolute_path = join(dirname(__file__), relative_path)

    with open(absolute_path) as data_file:
        return json.loads(data_file.read())


if __name__ == '__main__':
    try:
        # assert_valid_schema(_load_json_data("users.json"), "schema.json")
        assert_valid_schema(_load_json_data("recording.json"), "recording_schema3.json")
        print("All tests passed")
    except jsonschema.exceptions.ValidationError as ve:
        print("json schema validation error")
        print(ve.message)
        print(ve)
        pass
