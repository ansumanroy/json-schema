import json
import jsonschema


def test_get_user():
    file_object = open("/impl/data/users.json", 'r')
    json_data = json.loads(file_object.read())

    print(json_data)
    # assert 'data' in json_data
    # assert 'type' in json_data['data']
    # assert 'id' in json_data['data']
    # assert 'attributes' in json_data['data']
    # assert 'email' in json_data['data']['attributes']


if __name__ == '__main__':
    test_get_user()
