# metadata/metadata.py

import json

def load_json_dict(path, convert_keys_to_int=False):
    with open(path, 'r') as f:
        data = json.load(f)
    if convert_keys_to_int:
        return {int(k): v for k, v in data.items()}
    return data

# Load dictionaries
symptoms_dict = load_json_dict('metadata/symptoms.json')
diseases_list = load_json_dict('metadata/diseases.json', convert_keys_to_int=True)
