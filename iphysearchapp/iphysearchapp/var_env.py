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
INFOR = [['ping -b -c 100 -m 25 -vpn-instance', '', ''],
         ['display mac-address dy | i ', '', ''],
         ['display interface ', '', '']]

datosdeprueba = """pais;ip;nat-instance;access-user limit;port-limit;address-group;bind-ip-pool;IPs_Disponible;Posibles usuarios;Usuarios;Utilizacion Usuarios;Max por IP;location;trafico;capacidad;trafico global;capacidad global
GT;10.179.28.2;CGNAT_BRAS;150;4096;CGNAT_Pool_Group_1;CGNAT_Public_Pool_BRAS;2560;384000;37741;9.8%;0%;['Slot: 12 Engine: 0', 'Slot: 13 Engine: 0'];['15.05', '15.45'];['240', '240'];30.5;480.0
GT;10.179.28.2;CGNAT_HFC;75;4096;CGNAT_Pool_Group_2;CGNAT_Public_Pool_HFC;3584;268800;79976;29.7%;0%;['Slot: 1 Engine: 0', 'Slot: 1 Engine: 1', 'Slot: 3 Engine: 0', 'Slot: 3 Engine: 1', 'Slot: 10 Engine: 0', 'Slot: 10 Engine: 1', 'Slot: 11 Engine: 0', 'Slot: 11 Engine: 1'];['10.47', '11.0', '11.32', '11.55', '11.43', '11.25', '10.91', '11.22'];['40', '40', '40', '40', '40', '40', '40', '40'];89.15;320.0
GT;10.179.28.2;CGNAT_MOVIL;1200;4096;CGNAT_Pool_Group_MOVIL;CGNAT_Public_Pool_MOVIL;768;921600;0;0.0%;0%;['Slot: 1 Card: 0', 'Slot: 1 Card: 1', 'Slot: 2 Engine: 0', 'Slot: 2 Engine: 1', 'Slot: 2 Card: 0', 'Slot: 2 Card: 1', 'Slot: 3 Card: 0', 'Slot: 3 Card: 1', 'Slot: 10 Card: 0', 'Slot: 10 Card: 1', 'Slot: 11 Card: 0', 'Slot: 11 Card: 1'];['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0'];['40', '40', '40', '40', '40', '40', '40', '40', '40', '40', '40', '40'];0.0;480.0
GT;10.179.28.2;CGNAT_MOVIL_LTE;1800;4096;CGNAT_Pool_Group_MOVIL_LTE;CGNAT_Public_Pool_MOVIL_LTE;3072;5529600;1566302;28.3%;0%;['Slot: 1 Card: 0', 'Slot: 1 Card: 1', 'Slot: 2 Engine: 0', 'Slot: 2 Engine: 1', 'Slot: 2 Card: 0', 'Slot: 2 Card: 1', 'Slot: 3 Card: 0', 'Slot: 3 Card: 1', 'Slot: 10 Card: 0', 'Slot: 10 Card: 1', 'Slot: 11 Card: 0', 'Slot: 11 Card: 1'];['14.7', '15.01', '14.59', '14.46', '16.28', '16.2', '16.55', '15.6', '15.93', '16.32', '15.69', '15.46'];['40', '40', '40', '40', '40', '40', '40', '40', '40', '40', '40', '40'];186.79;480.0
GT;10.179.28.2;CGNAT_IPTV;128;4096;CGNAT_Pool_Group_IPTV;CGNAT_Public_Pool_IPTV;1024;131072;23244;17.7%;0%;['Slot: 12 Engine: 0', 'Slot: 13 Engine: 0'];['15.61', '16.82'];['240', '240'];32.43;480.0
GT;10.179.28.2;CGNAT_YOCOFON;65535;4096;CGNAT_Pool_Group_YOCOFON;CGNAT_Public_Pool_YOKOFON;256;16776960;0;0.0%;0%;['Slot: 1 Card: 0', 'Slot: 1 Card: 1', 'Slot: 2 Engine: 0', 'Slot: 2 Engine: 1', 'Slot: 2 Card: 0', 'Slot: 2 Card: 1', 'Slot: 3 Card: 0', 'Slot: 3 Card: 1', 'Slot: 10 Card: 0', 'Slot: 10 Card: 1', 'Slot: 11 Card: 0', 'Slot: 11 Card: 1'];['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0'];['40', '40', '40', '40', '40', '40', '40', '40', '40', '40', '40', '40'];0.0;480.0
GT;10.179.28.3;CGNAT_BRAS;150;4096;CGNAT_Pool_Group_1;CGNAT_Public_Pool_BRAS;2560;384000;26532;6.9%;0%;['Slot: 12 Engine: 0', 'Slot: 13 Engine: 0'];['7.68', '7.57'];['240', '240'];15.25;480.0
GT;10.179.28.3;CGNAT_HFC;75;4096;CGNAT_Pool_Group_2;CGNAT_Public_Pool_HFC;3584;268800;87890;32.6%;0%;['Slot: 1 Engine: 0', 'Slot: 1 Engine: 1', 'Slot: 3 Engine: 0', 'Slot: 3 Engine: 1', 'Slot: 10 Engine: 0', 'Slot: 10 Engine: 1', 'Slot: 11 Engine: 0', 'Slot: 11 Engine: 1'];['13.7', '13.04', '14.18', '13.14', '13.44', '13.44', '13.92', '13.43'];['40', '40', '40', '40', '40', '40', '40', '40'];108.28;320.0
GT;10.179.28.3;CGNAT_MOVIL;1200;4096;CGNAT_Pool_Group_MOVIL;CGNAT_Public_Pool_MOVIL;768;921600;0;0.0%;0%;['Slot: 1 Card: 0', 'Slot: 1 Card: 1', 'Slot: 2 Engine: 0', 'Slot: 2 Engine: 1', 'Slot: 2 Card: 0', 'Slot: 2 Card: 1', 'Slot: 3 Card: 0', 'Slot: 3 Card: 1', 'Slot: 10 Card: 0', 'Slot: 10 Card: 1', 'Slot: 11 Card: 0', 'Slot: 11 Card: 1'];['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0'];['40', '40', '40', '40', '40', '40', '40', '40', '40', '40', '40', '40'];0.0;480.0
GT;10.179.28.3;CGNAT_MOVIL_LTE;1800;4096;CGNAT_Pool_Group_MOVIL_LTE;CGNAT_Public_Pool_MOVIL_LTE;3328;5990400;1362161;22.7%;0%;['Slot: 1 Card: 0', 'Slot: 1 Card: 1', 'Slot: 2 Engine: 0', 'Slot: 2 Engine: 1', 'Slot: 2 Card: 0', 'Slot: 2 Card: 1', 'Slot: 3 Card: 0', 'Slot: 3 Card: 1', 'Slot: 10 Card: 0', 'Slot: 10 Card: 1', 'Slot: 11 Card: 0', 'Slot: 11 Card: 1'];['14.51', '13.11', '14.48', '13.06', '13.61', '13.84', '14.13', '14.2', '14.42', '14.1', '13.46', '12.7'];['40', '40', '40', '40', '40', '40', '40', '40', '40', '40', '40', '40'];165.62;480.0
GT;10.179.28.3;CGNAT_IPTV;128;4096;CGNAT_Pool_Group_IPTV;CGNAT_Public_Pool_IPTV;1024;131072;59627;45.4%;0%;['Slot: 12 Engine: 0', 'Slot: 13 Engine: 0'];['41.76', '41.88'];['240', '240'];83.64;480.0
GT;10.179.28.3;CGNAT_YOCOFON;65535;4096;CGNAT_Pool_Group_YOCOFON;CGNAT_Public_Pool_YOKOFON;256;16776960;0;0.0%;0%;['Slot: 1 Card: 0', 'Slot: 1 Card: 1', 'Slot: 2 Engine: 0', 'Slot: 2 Engine: 1', 'Slot: 2 Card: 0', 'Slot: 2 Card: 1', 'Slot: 3 Card: 0', 'Slot: 3 Card: 1', 'Slot: 10 Card: 0', 'Slot: 10 Card: 1', 'Slot: 11 Card: 0', 'Slot: 11 Card: 1'];['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0'];['40', '40', '40', '40', '40', '40', '40', '40', '40', '40', '40', '40'];0.0;480.0
GT;10.179.28.98;CGNAT_BRAS;150;4096;CGNAT_Pool_Group_1;CGNAT_PUBLIC_POOL_BRAS;512;76800;24880;32.3%;0%;['Slot: 12 Engine: 0', 'Slot: 13 Engine: 0'];['9.99', '10.11'];['160', '160'];20.1;320.0
GT;10.179.28.98;CGNAT_HFC;75;4096;CGNAT_Pool_Group_2;CGNAT_PUBLIC_POOL_HFC;256;19200;0;0.0%;0%;['Slot: 12 Engine: 0', 'Slot: 13 Engine: 0'];['0.0', '0.0'];['160', '160'];0.0;320.0
GT;10.179.28.98;CGNAT_GPON;150;4096;CGNAT_Pool_Group_3;CGNAT_PUBLIC_POOL_GPON;256;38400;14042;36.5%;0%;['Slot: 12 Engine: 0', 'Slot: 13 Engine: 0'];['5.65', '5.74'];['160', '160'];11.39;320.0
GT;10.179.28.99;CGNAT_BRAS;150;4096;CGNAT_Pool_Group_1;CGNAT_PUBLIC_POOL_BRAS;512;76800;12283;15.9%;0%;['Slot: 12 Engine: 0', 'Slot: 13 Engine: 0'];['4.34', '4.8'];['160', '160'];9.14;320.0
GT;10.179.28.99;CGNAT_HFC;75;4096;CGNAT_Pool_Group_2;CGNAT_PUBLIC_POOL_HFC;256;19200;0;0.0%;0%;['Slot: 12 Engine: 0', 'Slot: 13 Engine: 0'];['0.0', '0.0'];['160', '160'];0.0;320.0
GT;10.179.28.99;CGNAT_GPON;150;4096;CGNAT_Pool_Group_3;CGNAT_PUBLIC_POOL_GPON;256;38400;8202;21.3%;0%;['Slot: 12 Engine: 0', 'Slot: 13 Engine: 0'];['3.64', '4.1'];['160', '160'];7.74;320.0
GT;10.179.28.100;CGNAT_BRAS;150;4096;CGNAT_Pool_Group_1;CGNAT_PUBLIC_POOL_BRAS;512;76800;11282;14.6%;0%;['Slot: 12 Engine: 0', 'Slot: 13 Engine: 0'];['3.64', '4.29'];['160', '160'];7.93;320.0
GT;10.179.28.100;CGNAT_HFC;75;4096;CGNAT_Pool_Group_2;CGNAT_PUBLIC_POOL_HFC;256;19200;0;0.0%;0%;['Slot: 12 Engine: 0', 'Slot: 13 Engine: 0'];['0.0', '0.0'];['160', '160'];0.0;320.0
GT;10.179.28.100;CGNAT_GPON;150;4096;CGNAT_Pool_Group_3;CGNAT_PUBLIC_POOL_GPON;256;38400;12978;33.7%;0%;['Slot: 12 Engine: 0', 'Slot: 13 Engine: 0'];['6.68', '7.04'];['160', '160'];13.71;320.0
GT;10.179.28.101;CGNAT_BRAS;150;4096;CGNAT_Pool_Group_1;CGNAT_PUBLIC_POOL_BRAS;512;76800;12660;16.4%;0%;['Slot: 12 Engine: 0', 'Slot: 13 Engine: 0'];['5.04', '4.98'];['160', '160'];10.02;320.0
GT;10.179.28.101;CGNAT_HFC;75;4096;CGNAT_Pool_Group_2;CGNAT_PUBLIC_POOL_HFC;256;19200;0;0.0%;0%;['Slot: 12 Engine: 0', 'Slot: 13 Engine: 0'];['0.0', '0.0'];['160', '160'];0.0;320.0
GT;10.179.28.101;CGNAT_GPON;150;4096;CGNAT_Pool_Group_3;CGNAT_PUBLIC_POOL_GPON;256;38400;25816;67.2%;0%;['Slot: 12 Engine: 0', 'Slot: 13 Engine: 0'];['10.79', '12.06'];['160', '160'];22.85;320.0"""