import os

if os.path.exists(r"C:\\Users\\personal\\Desktop\\IPsCheck.txt"):
    os.remove(r"C:\\Users\\personal\\Desktop\\IPsCheck.txt")
else:
    new_file = open(r"C:\\Users\\personal\\Desktop\\IPsCheck.txt", "x")

file = open(r"C:\\Users\\personal\\Desktop\\IPs.txt","r+")

new_file = open(r"C:\\Users\\personal\\Desktop\\IPsCheck.txt", "x")

for line in file:
    response =  os.system("ping -n 2  " + line + "\n")
    if response == 0:
        print(line)
        new_file.write(line)
    else:
        print("Server not available ")