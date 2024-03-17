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
PASSWORDOWN = 'Alguno23'
HOSTOWN = '10.10.26.7'
DBOWN = 'ipsearch_db_new'


DBSINICIAL ='f%'
DBESUP = 'uptime'
INFOR = 'ping -b -c 100 -vpn-instance x.y.z.w'

DEVISUP = 'SELECT status FROM uptime WHERE uptime.ip LIKE %s'
RBSTXTFROM = "SELECT * FROM {}.nodob WHERE ip LIKE %s" 

CPETXT = """ SELECT * FROM (
    SELECT *, 'gt' AS table_name FROM {}.arp_gt
    UNION ALL
    SELECT *, 'sv' AS table_name FROM {}.arp_sv
    UNION ALL
    SELECT *, 'hn' AS table_name FROM {}.arp_hn
    UNION ALL
    SELECT *, 'ni' AS table_name FROM {}.arp_ni 
    UNION ALL
    SELECT *, 'cr' AS table_name FROM {}.arp_cr
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

datacrcgnat = [
    ["pais", "ip", "nat-instance", "access-user limit", "IPs_Disponible", "Posibles usuarios", "Usuarios", "Utilizacion Usuarios"],
    ["CR", "10.179.36.15", "CGNAT_HSI", 150, 200, 30000, 10443, "34.80%"],
    ["CR", "10.179.36.15", "CGNAT_MOVIL", 65535, 8, 524280, 0, "0.00%"],
    ["CR", "10.179.36.15", "CGNAT_MOVIL_LTE", 1400, 384, 537600, 214614, "39.90%"],
    ["CR", "10.179.36.15", "CGNAT_IPTV_GPON", 65535, 64, 4194240, 408, "0.00%"],
    ["CR", "10.179.36.15", "CGNAT_CR_PRIVADO", 180, 32, 5760, 5, "0.00%"],
    ["CR", "10.179.36.16", "CGNAT_HSI", 150, 200, 30000, 13051, "43.50%"],
    ["CR", "10.179.36.16", "CGNAT_MOVIL", 65535, 8, 524280, 0, "0.00%"],
    ["CR", "10.179.36.16", "CGNAT_MOVIL_LTE", 1400, 384, 537600, 213886, "39.70%"],
    ["CR", "10.179.36.16", "CGNAT_IPTV_GPON", 65535, 64, 4194240, 0, "0.00%"],
    ["CR", "10.179.36.16", "CGNAT_CR_PRIVADO", 180, 64, 11520, 8, "0.00%"]
    ]
