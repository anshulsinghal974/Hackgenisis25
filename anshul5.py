import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')  

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the Users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserName TEXT NOT NULL UNIQUE,
        Password TEXT NOT NULL,
        Email TEXT NOT NULL UNIQUE,
        InterestOption TEXT CHECK (InterestOption IN ('Volunteer', 'Donator'))
    )
''')

# Commit the changes to the database
conn.commit()

# Close the connection (optional, but good practice)
conn.close()