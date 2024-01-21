from netmiko import ConnectHandler

xdevice = {
    "device_type": "cisco_ios",
    "host": "10.195.9.148",
    "username": "navalos",
    "password": "!Megal0dont3",
}

command = "show version"
with ConnectHandler(**xdevice) as net_connect:
    output = net_connect.send_command(command)

print(output)

      