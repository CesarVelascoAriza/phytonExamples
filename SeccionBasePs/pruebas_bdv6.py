import psycopg2
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='localhost',
    port='5432',
    database='test'
    )

try:
    with conexion:
        with conexion.cursor() as cursor:
           sentencia = 'update persona set nombre =%s, apellido =%s email=%s where id_persna= %s'
           valores =('carlos','relara','clara@gmail.com',1)
           cursor.execute(sentencia,valores)
           registros_actualizados = cursor.rowcount
           print(f'registros actualizados {registros_actualizados}')
except Exception as e:
    print(f"ocurrio un error : {e} ")
finally:
    conexion.close()