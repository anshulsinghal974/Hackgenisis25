import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('health_data.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the HealthData table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS HealthData (
        RecordID INTEGER PRIMARY KEY AUTOINCREMENT,
        ExerciseTime TEXT,  -- Store as HH:MM:SS or similar format
        YogaTime TEXT,       -- Store as HH:MM:SS or similar format
        Mood TEXT,            -- E.g., "Happy", "Sad", "Stressed", etc.
        SleepHours REAL,      -- Number of hours slept
        SleepQuality TEXT,    -- E.g., "Good", "Poor", "Average", etc.
        StressLevel INTEGER,  -- Scale of 1 to 10 (or similar)
        WaterIntake REAL,    -- Liters of water consumed
        NutritionCalories INTEGER, -- Calories consumed
        EntryTime DATETIME DEFAULT CURRENT_TIMESTAMP  -- Time of data entry
    )
''')

# Commit the changes to the database
conn.commit()

# Close the connection (optional, but good practice)
conn.close()