#!/usr/bin/env python3

import json

def get_json_content(input_file: str):
    f = open(input_file, "r")
    json_content = json.load(f)
    return json_content

def extract_infos(json_content):
    result_data = []

    # 1st source of information : about time
    for split in json_content['fiche']['pass']['e']:
        # infos about the split in e['@attributes']
        result_data.append(split['@attributes'].copy())

    # offset if locations were not splited
    offset = 0

    # 2nd source of information : about the location
    for i, location in enumerate(json_content['fiche']['pts']['pt']):
        # infos about the split in pt['@attributes']

        # check if splitint point are in the same order :
        if(not (location['@attributes']['idpt'] == result_data[i - offset]["idpt"])):
            # the location has not being splited ... 
            offset += 1
            continue
            raise Exception("Problem with order !")
        
        # copy new (key, value) in the dict :
        for key, value in location['@attributes'].items():
            result_data[i - offset][key] = value

    return result_data

def create_json_file(content, output_file: str):
    f = open(output_file, "w")
    f.write(json.dumps(content, sort_keys=True, indent=4))

if "__main__" == __name__:
    json_content = get_json_content("./results.json")
    content = extract_infos(json_content)
    create_json_file(content, "./pretty_results.json")

