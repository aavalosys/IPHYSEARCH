from iphysearchapp.var_env import *
from django.conf import settings
from django.db import connection, connections
import time
import mysql.connector 

def conexion_dbbk(DBBACKUP):    #CONEXION BK 10.10.26.5 
    mydb = mysql.connector.connect(host= HOSTBACKUP, user= USERBACKUP, password=PASSWORDBACKUP, database=DBBACKUP, charset="utf8mb4")
    return  mydb
 
def conexion_dbnet(DB):     #CONEXION DATA 10.10.26.4
    mydb = mysql.connector.connect(host= HOST, user= USER, password=PASSWORD, database=DB, charset="utf8mb4")
    return  mydb

def conexion_dbown(DBOWN):  #CONEXION LOCAL 10.10.26.7
    mydb = mysql.connector.connect(host= HOSTOWN, user= USEROWN, password=PASSWORDOWN, database=DBOWN, charset="utf8mb4") 
    return  mydb

def esquemata_general():
    conn, cursor = establecer_conexion_mysql(HOST, USER, PASSWORD)
    if not conn or not cursor:
        raise Exception("No se pudo establecer la conexión a la base de datos")
    query = "SHOW DATABASES LIKE 'fy%'"
    cursor.execute(query)
    esquemas_g = cursor.fetchall()
    esquemas_generales = list(reversed(esquemas_g))
    cerrar_conexion_mysql(conn, cursor)
    esquemas_seleccionados = esquemas_generales[1:25]
    return esquemas_seleccionados

def establecer_conexion_mysql(servidor, usuario, contraseña, base_datos=None):
    try:
        conn = mysql.connector.connect(
            host=servidor,
            user=usuario,
            password=contraseña,
            database=base_datos if base_datos else None
        )
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        print(f"Error al establecer la conexión: {e}")
        return None, None
    
def cerrar_conexion_mysql(conn, cursor):
    try:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    except Exception as e:
        print(f"Error al cerrar la conexión: {e}")
