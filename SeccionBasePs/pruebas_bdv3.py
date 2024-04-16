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
            sentencia = 'select * from persona where id_persona in (1,2)'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            for registro in registros:
                print(registros)
except Exception as e:
    print(f"ocurrio un error : {e} ")
finally:
    conexion.close()