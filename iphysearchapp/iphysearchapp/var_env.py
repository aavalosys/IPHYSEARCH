DBMANTTOLOCAL = "dblocal_mantto"
DBBACKUP = 'temp_db'
DBOWN = 'ipsearch_db_new'  #CONEXION DATOS LOCAL 10.10.26.7
DBNEWLOCAL = 'dbloip130324' 
DBNEWLOCAL1 = "dblocalip06102024"

PORT = '3306'
ENGINE = 'django.db.backends.mysql'

USER = 'navalos'
PASSWORD = '44&7Ai0YHbD#'
HOST = '10.10.26.4' 
                
USERBACKUP = 'nelson.avalos'   
PASSWORDBACKUP = 'Navalos20230720#' 
HOSTBACKUP = '10.10.26.5'
      
USEROWN = 'nelson.avalos'
PASSWORDOWN = 'Alguno23'
HOSTOWN = '10.10.26.7' 


DBSINICIAL =''
DBSINICIALBACKUPS = 'nbk%'
DBSINICIALOWN = 'dbloip%'

DBESUP = 'uptime'

INFOR = [['ping -b -c 100 -m 25 -vpn-instance', '', ''],
         ['display mac-address dynamic | i ', '', ''],
         ['display interface ', '', '']]

USERVPNBUSCAR = 'buscarnodosip'
PASSVPNBUCAR = '@Ningun2024!'
EQUIPOVPNBUSCAR = 'huawei'

estados = ['ESTADO','OPEN', 'CLOSED']
vendors = ['VENDORS','AMX', 'LEVEL3', 'INOC','GOOGLE', 'NETFLIX', 'AKAMAI','TELXIUS', 'VERIZON', 'TATA', 'NTT','COGENT', 'TELIA', 'ARELION']
proveedores = ['PROVEEDORES','HUAWEI', 'CISCO', 'RAD','STG']
paises =  ['PAISES','GUATEMALA', 'EL SALVADOR', 'HONDURAS', 'NICARAGUA', 'COSTA RICA']
ndivisor=10
max_paginas=5





 