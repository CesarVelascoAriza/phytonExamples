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
            #llaves_primarias = ((1,2,3,4),)
            entrada = input('proporcionar los id \'s a buscar separadas por (,):')
            llaves_primarias = (tuple(entrada.split(",")),)
            sentencia = 'select * from persona where id_persona in %s'
            cursor.execute(sentencia,llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registros)
except Exception as e:
    print(f"ocurrio un error : {e} ")
finally:
    conexion.close()