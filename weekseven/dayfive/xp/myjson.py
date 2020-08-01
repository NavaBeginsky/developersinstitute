import json

with open('myjson.JSON', 'r') as jfile:
	data = json.load(jfile)

print(data['company']['employee']['payble']['salary'])


sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
sampleJsonSorted = {k:sampleJson[k] for k in sorted(sampleJson)}
# It says to sort it in the python file so I wasnt sure if that meant to do what I
#did above or to add the sort_keys=True to the dump
with open('myjson.json', 'a') as jfile:
	json.dump(sampleJsonSorted, jfile, indent=4)