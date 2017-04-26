import json

from pprint import pprint

with open('vibez.json') as data_file:
    data = json.load(data_file)

node = input()
list = data[node].split()

pprint(data[node])

print("\n")


for i in list:
    data1 = data[i]
    pprint(data1)
    print("\n")
    print("-----------------------------------------------------------------------")


