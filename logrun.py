import sqlite3

db_path = "data/run_logs2.db"
current_goal = None

# Initialize the database and create tables if they don't exist
conn = sqlite3.connect(db_path)
conn.execute("""
CREATE TABLE IF NOT EXISTS goals (
    distance REAL
)""")
conn.execute("""
CREATE TABLE IF NOT EXISTS runs (
    name TEXT,
    date TEXT,
    distance REAL,
    time INTEGER,
    mood TEXT
)""")
conn.close()

# Function to log a run
def log_run(name, date, distance, time, mood):
    global current_goal
    
    if current_goal is None:
        conn = sqlite3.connect(db_path)
        current_goal = conn.execute("SELECT distance FROM goals").fetchone() # Fetch current goal
        conn.close()
        if current_goal:
            current_goal = current_goal[0]
        else:
            return "Please set a goal first"
    
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("""
        INSERT INTO runs VALUES (?, ?, ?, ?, ?)
        """, (name, date, float(distance), int(time), mood))
        conn.commit()
        conn.close()
        
        if float(distance) >= current_goal:
            return "Run logged! Goal met!"
        else:
            return "Run logged! Goal not met."
    except Exception as e:
        return f"Could not save run: {e}"