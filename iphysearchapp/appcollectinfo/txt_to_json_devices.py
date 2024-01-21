import json


ipdevices = 'F:\\PYPROJECTS\\NET_SCANN\\ipdevices.txt'
jsonipdevices = {}

with open(ipdevices) as file:

	for line in file:
		id, description = line.strip().split(None, 2)
		print(description+""+id)
		jsonipdevices[id] = description.strip()


out_file = open("F:\\PYPROJECTS\\NET_SCANN\\jsonipdevices_info.json", "w")
json.dump(jsonipdevices, out_file, indent = 4, sort_keys = False)
out_file.close()
