import json
with open('ex.json', 'r') as f:
    data = f.read()
    json_data = json.loads(data)
    print(type(json_data))
    print(json_data)
    print(json_data['children'])
    print(json_data['children'][1]['firstName'],
    json_data['children'][1]['age'])