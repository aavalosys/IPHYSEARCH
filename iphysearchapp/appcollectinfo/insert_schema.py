import os
import mysql.connector

mydb = mysql.connector.connect(host= '10.10.26.7', user= 'navalos', password='44&7Ai0YHbD#', database='nw_db_ipsearch')
mycursor = mydb.cursor()
current_dir = os.getcwd()
print (current_dir + "\insert_schema.py")
#for line in open(script_path).readlines():
     #mycursor.execute(line)
        
mydb.close()