import os   ### para pruebas de ping
import time
from netmiko import Netmiko
from netmiko import ConnectHandler
import sys

def pingstatus(ip):
    # response = os.popen(f"ping {ip} -c 4").read() #macbook 
    response = os.popen(f"ping {ip} -n 4").read()  #windows
    # windows
    if "0% perdidos" in response:
        return True
    else:
        return False
    #CODIGO PARA MACBOOK
    # if ', 0.0% packet loss' in response:
        # return True
    # else:
        # return False


def cisco_connect(ip_address, user, passwd):
    element_connection = None
    if pingstatus(ip_address):
        try:
            element_connection = ConnectHandler(device_type='cisco_ios', host=ip_address, username=user,password=passwd, global_delay_factor=3, conn_timeout = 10)
            # element_connection = ConnectHandler(device_type='cisco_ios_telnet', host=ip_address, username=user,password=passwd, global_delay_factor=2)
             #element_connection = ConnectHandler(device_type='huawei', host=ip_address, username=user,password=passwd, global_delay_factor=3)
        except :
            pass
            #print(Exception)
        if element_connection != None:
            return element_connection
        else:
            try:          
                element_connection = ConnectHandler(device_type='cisco_ios_telnet', host=ip_address, username=user,password=passwd, global_delay_factor=3, conn_timeout = 10)
                # element_connection = ConnectHandler(device_type='cisco_ios', host=ip_address, username=user,password=passwd, global_delay_factor=2)
            except :
                pass
                #print(Exception)
            if element_connection != None:
                return element_connection
            else:
                return False
    else:
        return False
        

def ger_version(element_connection,worker):
    try:
        show_version_return = element_connection.send_command("show ver")
    except Exception as e:
        print("\nHUBO UN PROBLEMA AL INTENTAR OBTENER LA VERSION en :"+ worker)
        return False
    show_version_return_lines = show_version_return.splitlines()
    ios_version = ""
    if "Cisco IOS XE Software".upper() in show_version_return.upper():
        ios_version = "ios-xe"
    elif "Cisco IOS Software, IOS-XE Software".upper() in show_version_return.upper():
        ios_version = "ios-xe"
    elif "Cisco IOS XR Software".upper() in show_version_return.upper():
        ios_version = "ios-xr"
    elif "Cisco IOS Software".upper() in show_version_return.upper():
        ios_version = "ios"
    elif "IOS (tm)".upper() in show_version_return.upper():
        ios_version = "ios"
    else:
        show_version_return = element_connection.send_command("screen-length 0 temporary")
        show_version_return = element_connection.send_command("display version")
        show_version_return_lines = show_version_return.splitlines()
        if "VRP".upper() in show_version_return.upper() and "V300".upper() in show_version_return.upper() :
            ios_version = "vrp300"
        elif "VRP".upper() in show_version_return.upper() and "V200".upper() in show_version_return.upper() :
            ios_version = "vrp200"
        elif "VRP".upper() in show_version_return.upper() and "V600".upper() in show_version_return.upper() :
            ios_version = "vrp600"
        elif "VRP".upper() in show_version_return.upper() and "V800".upper() in show_version_return.upper() :
            ios_version = "vrp800"
        else: 
            print("No se encontro version:"+worker)
            print(show_version_return)
            #Failed to pass the authorization
    return ios_version


def closecon (element_connection,ip):
    desconexion = element_close(element_connection)
    if desconexion:
        #print(threading.current_thread().name,'Work Done, Session Close on   : ' + ip)
        #sys.stdout.write(threading.current_thread().name + ' Work Done, Session Close on   : ' + ip)
        sys.stdout.write('Work Done, Session Close on   : ' + ip)
        sys.stdout.write('\n')
        sys.stdout.flush()
    else:
        #print(threading.current_thread().name,'Work Done, Problem Clossing session on : ' + ip)
        #sys.stdout.write(threading.current_thread().name +' Work Done, Problem Clossing session on : ' + ip)
        sys.stdout.write('Work Done, Problem Clossing session on : ' + ip)
        sys.stdout.write('\n')
        sys.stdout.flush()

def element_close(element_connection):
	descone = False
	try:
		element_connection.disconnect()
		descone = True
	except Exception as e:
		 pass
	return descone