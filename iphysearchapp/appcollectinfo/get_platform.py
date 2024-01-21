from netmiko import ConnectHandler, SSHDetect

device = {
    "device_type": "autodetect",
    "ip": "10.130.15.168",
    "username": "navalos",
    "password": "%Osciloscopio100$",
    }

def DETECCION(device):
    guesser = SSHDetect(**device)
    best_match = guesser.autodetect()
    print(best_match)

DETECCION(device)
