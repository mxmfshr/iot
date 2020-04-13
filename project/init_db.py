import sqlite3

conn = sqlite3.connect('./db.sqlite')

cursor = conn.cursor()

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  card_id INTEGER,
  card_text TEXT,
  last_used TEXT,
  status TEXT
);
"""

create_authorized_users_table = """
CREATE TABLE IF NOT EXISTS authorized_users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  card_id INTEGER
);
"""

create_users = """
INSERT INTO
  users (card_id, card_text, last_used, status)
VALUES
  (123, '', '01:23, 5 April 2020, test', 'out'),
  (456, '', '12:34, 9 April 2020, test', 'out')
"""

create_authorized_users = """
INSERT INTO
  authorized_users (card_id)
VALUES
 (123)
"""

cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute(create_users_table)
cursor.execute(create_users)
cursor.execute("DROP TABLE IF EXISTS authorized_users")
cursor.execute(create_authorized_users_table)
cursor.execute(create_authorized_users)

conn.commit()
cursor.close()

