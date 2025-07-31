import sqlite3

db_path = "data/run_logs.db"

def setup_goal_table():
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS goals (
            weekly_distance REAL
        );
    """)

    connection.commit()
    connection.close()

setup_goal_table()

# Save or update the goal
def set_user_goal(weekly_distance):
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # only one goal is stored
        cursor.execute("DELETE FROM goals")
        cursor.execute("INSERT INTO goals (weekly_distance) VALUES (?)", (float(weekly_distance),))

        connection.commit()
        connection.close()
        return "Goal set successfully!"
    except Exception as e:
        return f"Could not set goal: {e}"
