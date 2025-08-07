import sqlite3

# Function to set a user goal
def set_user_goal(distance):
    try:
        distance = float(distance)
        conn = sqlite3.connect("data/run_logs2.db")
        
        # Clear old goals and save new one
        conn.execute("DELETE FROM goals")
        conn.execute("INSERT INTO goals VALUES (?)", (distance,))
        conn.commit()
        conn.close()
        
        return f"Goal set to {distance} km!"
    except Exception as e:
        return f"Could not set goal: {e}"