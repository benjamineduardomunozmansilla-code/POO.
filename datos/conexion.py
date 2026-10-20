from peewee import MySQLDatabase

base_datos = MySQLDatabase(
    'biblioteca_db',
    user='root',
    password='',
    host='localhost',
    port=3306
)

db = base_datos