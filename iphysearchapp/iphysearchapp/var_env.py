USER = 'navalos'
PASSWORD = '44&7Ai0YHbD#'
ENGINE = 'django.db.backends.mysql'
HOST = '10.10.26.4'
PORT = '3306'

USERBK = 'nelson.avalos'
PASSWORDBK = 'Navalos20230720#'
HOSTBK = '10.10.26.5'
DBBK = 'temp_db'

DBSINICIAL ='f%'

INFOR = 'ping -b -c 100 -vpn-instance x.y.z.w'
QUERBSTXT = "SELECT * FROM {}.nodob WHERE nodoid LIKE %s"
QUECPETXT = "SELECT * FROM (SELECT * FROM  {}.arp_gt UNION SELECT * FROM  {}.arp_sv UNION  SELECT * FROM  {}.arp_hn UNION SELECT * FROM  {}.arp_ni UNION  SELECT * FROM  {}.arp_cr ) as resultado where resultado.ipcpe like %s"