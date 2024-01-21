#GENERADOR DE ARCHIVO HOST A PARTIR DEL BACKUP ARCHIVO ACS
import os,re

if os.path.exists(r"F:\\PYPROJECTS\\NET_SCANN\\ipdevices.txt"):   #IF PATH EXIST REMOVE IT
    os.remove(r"F:\\PYPROJECTS\\NET_SCANN\\ipdevices.txt")
else:
    f = open(r"F:\\PYPROJECTS\\NET_SCANN\\ipdevices.txt", "x")    #CREATE FILE
    f.close()
c = 0         
f = open(r"F:\\PYPROJECTS\\NET_SCANN\\ipdevices.txt","a")         #OPEN FILE

for backups, dirs, archivos in os.walk("F:\\PYPROJECTS\\NET_SCANN\\Backup_dev\\"): #UBICACION ARCHIVO BACKUP
    for backups in archivos:
        if backups.endswith(".txt"): 
            name = str(backups)[::-1]             #INVIERTE STRING PARA LECTURA DERECHA - IZQUIERDA
            ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",name)   #EXTRACT IP FROM STRING
            namefile = str(ip).replace("['", '')   #REMOVE [
            namefilee = namefile.replace("']",'')  #REMOVE 
            namefilee = namefilee[::-1]            #INVIERTE ARCHIVO PARA CONVERTIRLO ORIGINALMENTE
            print(str(c)+" "+namefilee +"\n")
            c += 1
            f.write(str(c)+" "+namefilee +"\n")
            
            
            