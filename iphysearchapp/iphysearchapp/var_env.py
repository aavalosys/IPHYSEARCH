USER = 'navalos'
PASSWORD = '44&7Ai0YHbD#'
ENGINE = 'django.db.backends.mysql'
HOST = '10.10.26.4'
PORT = '3306'

USERBK = 'nelson.avalos'
PASSWORDBK = 'Navalos20230720#'
HOSTBK = '10.10.26.5'
DBBK = 'temp_db'

USEROWN = 'nelson.avalos'
PASSWORDOWN = 'Navalos20230720#'
HOSTOWN = '10.10.26.7'
DBOWN = 'ipsearch_db_new'


DBSINICIAL ='f%'
DBESUP = 'uptime'
INFOR = 'ping -b -c 100 -vpn-instance x.y.z.w'

DEVISUP = 'SELECT status FROM uptime WHERE uptime.ip LIKE %s'
RBSTXTFROM = "SELECT * FROM {}.nodob WHERE ip LIKE %s" #BUSCA ELEMENTO NEMONICO

CPETXT = """ SELECT * FROM (
    SELECT *, 'GT' AS table_name FROM {}.arp_gt
    UNION ALL
    SELECT *, 'SV' AS table_name FROM {}.arp_sv
    UNION ALL
    SELECT *, 'HN' AS table_name FROM {}.arp_hn
    UNION ALL
    SELECT *, 'NI' AS table_name FROM {}.arp_ni 
    UNION ALL
    SELECT *, 'CR' AS table_name FROM {}.arp_cr
) AS resultado WHERE resultado.ipcpe LIKE %s
"""

CPEARP = """ SELECT * FROM (
    SELECT *, 'GT' AS table_name FROM {}.arp_gt
    UNION ALL
    SELECT *, 'SV' AS table_name FROM {}.arp_sv
    UNION ALL
    SELECT *, 'HN' AS table_name FROM {}.arp_hn
    UNION ALL
    SELECT *, 'NI' AS table_name FROM {}.arp_ni 
    UNION ALL
    SELECT *, 'CR' AS table_name FROM {}.arp_cr
) AS resultado WHERE resultado.mac LIKE %s
"""

#NO EN USO ACTUALMENTE
SERVNORMALMAC = """SELECT m.*, i.description FROM {}.mac_address_cr m  
                  JOIN {}.int_cr i ON m.ip = i.ip AND m.interface = i.interface
                  WHERE mac LIKE "%{}%" AND vlan = "{}"
                  ORDER BY count ASC"""

TIPOSERVICIOTXT = "SELECT * FROM {}.nodob WHERE nodoid LIKE %s"

PATHTXT =""

 