import psycopg2
import colorsys
from config import *

try:
    #connect to DB
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
    
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT version();'
        )
        print(f'Server version: {cursor.fetch}')

except Exception as _ex:
    print('[INFO] Error while working with PostgreSQL')
finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connection closed')