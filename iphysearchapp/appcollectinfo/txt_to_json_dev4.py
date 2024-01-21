import json


ipdevices = 'F:\\PYPROJECTS\\NET_SCANN\\ipdevices.txt'
jsonipdevices = {}
atributos =['nemonico', 'vendor', 'version', 'modelo', 'grupo', 'activo']
with open(ipdevices) as file:
	for line in file:
		id, description = line.strip().split(None, 6)
		print(description)

        sno ='emp'+str(l)
        i = 0
            while i<len(fields):
             
                dict2[fields[i]]= description[i]
                i = i + 1
                 
        # appending the record of each employee to
        # the main dictionary
        dict1[sno]= dict2
        l = l + 1
 
 
# creating json file       
out_file = open("test2.json", "w")
json.dump(dict1, out_file, indent = 4)
out_file.close()