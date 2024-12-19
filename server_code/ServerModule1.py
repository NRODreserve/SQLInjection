import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#



# Datenbank-Verbindung
db = sqlite3.connect(":memory:")  # Temporäre In-Memory-Datenbank (nur für Übungen)
cursor = db.cursor()

# Beispiel-Datenbank einrichten
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT,
    balance INTEGER
)
""")
cursor.executemany("""
INSERT INTO users (username, password, balance) VALUES (?, ?, ?)
""", [
    ("user1", "password1", 100),
    ("user2", "password2", 200),
    ("admin", "test123", 1000000),
])
db.commit()


@anvil.server.callable
def check_login(username, password):
    # Unsicherer SQL-Befehl (zu Demonstrationszwecken)
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print(f"SQL Query: {query}")  # Debugging

    cursor.execute(query)
    results = cursor.fetchall()

    # Ergebnisse als Liste von Dictionaries zurückgeben
    if results:
        return [{"account_id": r[0], "balance": r[3]} for r in results]
    else:
        return None
