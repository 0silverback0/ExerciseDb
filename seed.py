import sqlite3
import json

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Example: Fetch all data from the 'exercise' table
cursor.execute('SELECT * FROM exercises_exercise')
exercise_data = cursor.fetchall()

# Format the data (convert to a list of dictionaries)
formatted_exercise_data = [
    {
        'name': row[1],
        'primary_muscle': row[2],
        'exercise_type': row[3],
        'other_names': row[4],
        'image_url': row[5],
        'video_url': row[6],
        'instructions': row[7],
        'equipment': row[8]
    }
    for row in exercise_data
]

# Write the data to a JSON file (seed file)
with open('exercises/management/commands/exercise_seed_data.json', 'w') as file:
    json.dump(formatted_exercise_data, file, indent=2)

# Close the database connection
conn.close()
