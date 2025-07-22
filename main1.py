import sqlite3

db_path = "run_logs.db"

def setup_database():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            date TEXT,
            distance REAL,
            time INTEGER,
            goal REAL,
            goal_met TEXT,
            mood TEXT
        );
    """)
    conn.commit()
    conn.close()

# Call setup when app starts
setup_database()

def log_run(name, date, distance, time, goal, goal_met, mood):
    if not name:
        return "Please enter your name."

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO runs (name, date, distance, time, goal, goal_met, mood)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (name, date, float(distance), int(time), float(goal), goal_met, mood))
        conn.commit()
        conn.close()
        return "Run saved to database successfully!"
    except Exception as e:
        return f"Could not save run: {e}"
    
    
