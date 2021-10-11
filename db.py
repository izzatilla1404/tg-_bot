import types
from aiogram import bot
from aiogram.types import message
from aiohttp.helpers import ProxyInfo
import mysql.connector
from mysql.connector import Error
# import bot
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", "root", "Qwerty123$", "aaa")

# def create_database(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         print("Database created successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")

# def create_database_query(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.executor(query)
#         print("CREATE DATABASE sm_app")
#     except Error as e:
#         print(f"The error '{e}' occured")


# def execute_query(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         connection.commit()
#         print("Query executed successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")

# create_users_table = """
# CREATE TABLE IF NOT EXISTS users (
#   id INT AUTO_INCREMENT, 
#   gmail TEXT NOT NULL,  
#   PRIMARY KEY (id)
# ) ENGINE = InnoDB
# """

# execute_query(connection, create_users_table)

# create_users = """
# INSERT INTO
#   `users` (`gmail`)
# VALUES
#   ('James'),
#   ('Leila'),
#   ('Brigitte'),
#   ('Mike'),
#   ('Elizabeth');
# """

# execute_query(connection, create_users)  

# def execute_read_query(connection, query):
#     cursor = connection.cursor()
#     result = None
#     try:
#         cursor.execute(query)
#         result = cursor.fetchall()
#         return result
#     except Error as e:
#         print(f"The error '{e}' occurred")
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occured")

select_users = "SELECT * FROM users"
users = execute_read_query(connection, select_users)
list = []
for user in users:
    list.append(user)
print(list)

# SELECT `vdscontract`.`vdshostname`, `vds_tariffs`.`tariffname` FROM `user`, `vdscontract`, `vds_tariffs` WHERE `user`.`username` = 'marat@hostmaster.uz' AND `user`.`id` = `vdscontract`.`user_id` AND `vdscontract`.`vdsid` = `vds_tariffs`.`idvds` ORDER BY `vdscontract`.`vdshostname`;

# import pymysql
# from config import host, user, password, db
# try:
#     connection = pymysql.connect(
#         host=host,
#         port=3306,
#         user=user,
#         password=password,
#         database=db,
#         cursorclass=pymysql.cursors.DictCursor
#     )
#     print("Successfully connected...")  
    # print("#" * 20)
    
    # try:
    #     with connection.cursor() as cursor:
    #         insert_query = "INSERT INTO 'users' (email, password) VALUES ('izzat', '123');"
    #         cursor.execute(insert_query)
    #         connection.commit()
    # finally:
    #     connection.close()

# except Exception as ex:
#     print("Connection refused...")
#     print(ex)

# "SELECT 'users'.'email' FROM 'users' WHERE 'users'.'email'"