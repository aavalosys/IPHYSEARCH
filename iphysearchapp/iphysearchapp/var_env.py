USER = 'navalos'
PASSWORD = '44&7Ai0YHbD#'
ENGINE = 'django.db.backends.mysql' 
HOST = '10.10.26.4'
PORT = '3306'                #CONEXION DATA 10.10.26.4

USERBK = 'nelson.avalos'   
PASSWORDBK = 'Navalos20230720#'
HOSTBK = '10.10.26.5'
DBBK = 'temp_db'            #CONEXION BACKUPS 10.10.26.5 

USEROWN = 'nelson.avalos'
PASSWORDOWN = 'Alguno23'
HOSTOWN = '10.10.26.7'
DBOWN = 'ipsearch_db_new'  #CONEXION DATOS LOCAL 10.10.26.7
DBNEWLOCAL = 'dbloip130324'

DBSINICIAL ='f%'
DBSINICIALOWN = 'dbloip%'
DBESUP = 'uptime'

INFOR = [['ping -b -c 100 -m 25 -vpn-instance', '', ''],
         ['display mac-address dynamic | i ', '', ''],
         ['display interface ', '', '']]

USERVPNBUSCAR = 'buscarnodosip'
PASSVPNBUCAR = '@Ningun2024!'
EQUIPOVPNBUSCAR = 'huawei'


