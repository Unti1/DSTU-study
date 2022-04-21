import psycopg2
from config import *

def products_insetr(prodname,unitprod,datetime,datebreak,prodmake):
    with connection.cursor() as cursor:
        cursor.execute(
            f'''
            INSERT INTO products(product_name,product_unti,date_delivery,date_break,product_maker) VALUES
            ({prodname},{unitprod},DATE {datetime},{datebreak},{prodmake}); 
            '''
        )
        print("[INFO] Data has been upload into the table")


try:
    #connect to DB
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
    
    # Autoupdate changes
    connection.autocommit = True

    # Out Version of PostgreSQL
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT version();'
        )
        print(f'Server version: {cursor.fetchone()}')

    # Create new database
    with connection.cursor() as cursor:
        try:
            cursor.execute(
                '''CREATE TABLE products(
                    id serial PRIMARY KEY,
                    product_name varchar(255) NOT NULL,
                    product_unti varchar(20) NOT NULL,
                    date_delivery date NOT NULL,
                    product_maker varchar(255) NOT NULL,
                    date_of_break date NOT NULL);
                '''
            )
            print('[INFO] Table has been created')
        except:
            print("[INFO] Table are already create")
    # products_insert
except Exception as _ex:
    print('[INFO] Error while working with PostgreSQL')
finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connection closed')