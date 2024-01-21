import mysql.connector

# Datos de conexión a la base de datos
db_config = {
    'host': '10.10.26.5',
    'user': 'nelson.avalos',
    'password': 'Navalos20230720#',
    'database': 'temp_db',
}

try:
    # Conexión a la base de datos
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        print('Conexión exitosa a la base de datos MySQL!')

        # A partir de aquí, puedes realizar operaciones con la base de datos

        # Ejemplo: Obtener información de una tabla
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM backups_ip;')
        result_set = cursor.fetchall()

        for row in result_set:
            print(row)

        # Cerrar el cursor y la conexión
        cursor.close()

    else:
        print('Error en la conexión a la base de datos.')

except mysql.connector.Error as e:
    print(f'Error en la conexión a la base de datos: {e}')

finally:
    # Cerrar la conexión
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print('Conexión cerrada.')
