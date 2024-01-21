from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_dispatcher import ConnectHandler


ipdevices = open('F:\\PYPROJECTS\\NET_SCANN\\ipdevices.txt', 'r')
lineas = ipdevices.readlines()
 
count = 0
# Strips the newline character
for line in lineas:
    count += 1
    print("Line{}: {}".format(count, line.strip()))

#remote_device = {'device_type': 'autodetect',
 #                    'host': '10.39.152.167',
  #                   'username': 'navalos',
   #                  'password': '!Megal0dont3'}

#guesser = SSHDetect(**remote_device)
#best_match = guesser.autodetect()
#print(best_match) # Name of the best device_type to use further
#print(guesser.potential_matches) # Dictionary of the whole matching result