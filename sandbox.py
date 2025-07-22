import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('students.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Step 1: Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# Step 2: Insert a student
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Alice", 21))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Bob", 23))




# Step 3: Commit the changes
conn.commit()

# Step 4: Read and display all records
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("Student Records:")
for row in rows:
    print(row)

# Step 5: Close the connection
conn.close()
