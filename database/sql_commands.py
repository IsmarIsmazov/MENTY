import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create(self):
        if self.connection:
            print('Database connected')
        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)

    def sql_insert_user_telegram(self, telegram_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, telegram_id, username, first_name, last_name, 0)
        )
        self.connection.commit()

    def sql_select_user_command(self):
        users = self.cursor.execute(
            sql_queries.SELECT_USER_QUERY
        )
        return users.fetchall()

    def sql_update_user_count_command(self, telegram_id):
        self.cursor.execute(
            sql_queries.UPDATE_USER_COUNT_QUERY,
            (telegram_id,)
        )
        self.connection.commit()

    def sql_update_user_count_minus_command(self, telegram_id):
        self.cursor.execute(
            sql_queries.UPDATE_USER_COUNT_MINUS_QUERY,
            (telegram_id,)
        )
        self.connection.commit()
