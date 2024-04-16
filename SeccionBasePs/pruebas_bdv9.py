import psycopg2
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='localhost',
    port='5432',
    database='test'
    )
#actualizacion de varios registros
try:
    with conexion:
        with conexion.cursor() as cursor:
           sentencia = 'delete from persona where id_persona in %s'
           entrada = input('proporciona los id a eliminar (separados con coma): ')
           valores =(tuple(entrada.split(',')),)
           cursor.executemany(sentencia,valores)
           registros_eliminados = cursor.rowcount
           print(f'registros eliminados {registros_eliminados}')
except Exception as e:
    print(f"ocurrio un error : {e} ")
finally:
    conexion.close()