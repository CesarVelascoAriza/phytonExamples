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
            id_persona =1
            sentencia = 'select * from persona where id_persona = %s'
            cursor.execute(sentencia,(id_persona,))
            #registros = cursor.fetchall()
            registros = cursor.fetchone()
            print(registros)
except Exception as e:
    print(f"ocurrio un error : {e} ")
finally:
    conexion.close()
