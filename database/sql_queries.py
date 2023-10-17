CREATE_USER_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS telegram_users
        (ID INTEGER PRIMARY KEY,
         TELEGRAM_ID INTEGER,
         USERNAME CHAR(50),
         FIRST_NAME CHAR(50),
         LAST_NAME CHAR(50),
         COUNT INTEGER,
         UNIQUE(TELEGRAM_ID))
"""
INSERT_USER_QUERY = """INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?,?)"""
SELECT_USER_QUERY = """SELECT * FROM telegram_users"""
UPDATE_USER_COUNT_QUERY = """UPDATE telegram_users SET COUNT = COUNT + 1 WHERE TELEGRAM_ID = ?"""
UPDATE_USER_COUNT_MINUS_QUERY = """UPDATE telegram_users SET COUNT = COUNT - 1 WHERE TELEGRAM_ID = ?"""
