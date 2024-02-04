import json
import os


# returns the JSON data of the '../data/<filename.json>' sys-query
def readJson(filename: str):
    path = os.path.join(os.path.dirname(__file__), '..', 'data', filename)
    with open(path) as jsonFile:
        return json.load(jsonFile)
    