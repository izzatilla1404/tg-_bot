# import sqlite3

# class Database:
#     def __init__(self, db_file):
#         self.connection = sqlite3.connect(db_file)
#         self.cursor = self.connection.cursor()

#     def add_user(self, user_id):
#         with self.connection:
#             self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))
#         # result = self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))
#         # return bool(len(result.fetchall()))

#     def user_exists(self, user_id):
#         with self.connection:
#             result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchall()
#             return bool(len(result))

# def get_user_id(self, user_id):
#     result = self.cursor.execute("SELECT 'id' FROM 'users' WHERE 'user_id' = ?",(user_id))
#     return bool(len(result.fetchall()))

# def set_nickname(self, user_id, gmail):
#     with self.connection:
#         return self.cursor.execute("UPDATE 'users' SET 'gmail' = ? WHERE 'user_id' = ?", (gmail, user_id,))

# def get_signup(self, user_id):
#     with self.connection:
#         result = self.cursor.execute("SELECT 'signup' FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchall()
#         for row in result:
#             signup = str(row[0])
#         return signup

# def set_signup(self, user_id, signup):
#     with self.connection:
#         return self.cursor.execute("UPDATE 'users' SET 'signup' = ? WHERE 'user_id' = ?", (signup, user_id,))