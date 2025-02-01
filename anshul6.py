import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('volunteers.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the Volunteers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Volunteers (
        VolunteerID INTEGER PRIMARY KEY AUTOINCREMENT,
        VolunteerName TEXT NOT NULL,
        ContactDetails TEXT,
        AvailableWorkTime TEXT  -- Store as a string (e.g., "9am-5pm", "Weekends")
    )
''')

# Commit the changes to the database
conn.commit()

# Close the connection (optional, but good practice)
conn.close()