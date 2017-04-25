import json
from pprint import pprint

with open('vibez.json') as data_file:
    data = json.load(data_file)

node = input()

pprint(data[node])

