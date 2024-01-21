from netmiko import ConnectHandler

cisco1 = {
    "device_type": "cisco_ios",
    "host": "10.72.43.6",
    "username": "navalos",
    "password": "%Osciloscopio100$",
}
command = "terminal lenght 0 "
command = "show mac-address"
with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)

print(output)
print() 