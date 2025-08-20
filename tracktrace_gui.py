from tkinter import *
from tkinter import ttk, messagebox
from logrun import *
from setgoal import *
import sqlite3

root = Tk()
root.title("Tracktrace: Running App")
root.geometry("400x750")
root.configure(bg="#34324A")
root.resizable(False, False)

# Function to fetch runs from database
def fetch_runs():
    try:
        conn = sqlite3.connect("data/run_logs2.db")
        cursor = conn.cursor()
        cursor.execute("SELECT rowid, * FROM runs")
        runs = cursor.fetchall()
        conn.close()
        
        # Check if goal was met for each run
        goal = fetch_current_goal()
        runs_with_goal_status = []
        for run in runs:
            run_list = list(run)
            if goal and float(run[3]) >= goal:
                run_list.append("Yes")
            else:
                run_list.append("No")
            runs_with_goal_status.append(run_list)
            
        return runs_with_goal_status
    except Exception as e:
        messagebox.showerror("Database Error", f"Could not fetch runs: {e}")
        return []

# Function to fetch current goal
def fetch_current_goal():
    try:
        conn = sqlite3.connect("data/run_logs2.db")
        cursor = conn.cursor()
        cursor.execute("SELECT distance FROM goals")
        goal = cursor.fetchone()
        conn.close()
        return goal[0] if goal else None
    except:
        return None

# Functions
def on_log_run():
    form_win = Toplevel(root)
    form_win.title("Log a Run")
    form_win.geometry("350x500")
    form_win.configure(bg="#34324A")
    form_win.resizable(False, False)

    def submit_run():
        name = name_entry.get()
        date = date_entry.get()
        distance = distance_entry.get()
        time = time_entry.get()
        mood = mood_entry.get()

        if not all([name, date, distance, time, mood]):
            messagebox.showerror("Error", "Please fill all fields")
            return

        result = log_run(name, date, distance, time, mood)
        messagebox.showinfo("Result", result)
        form_win.destroy()
        refresh_runs_table()  # Refresh the table after adding a new run

    def make_label_entry(text):
        Label(form_win, text=text, bg="#34324A", fg="white", anchor="w").pack(fill=X, padx=10)
        entry = Entry(form_win, relief=FLAT, bg="white")
        entry.pack(fill=X, padx=10, pady=(0, 10))
        return entry

    name_entry = make_label_entry("Name")
    date_entry = make_label_entry("Date")
    distance_entry = make_label_entry("Distance (km)")
    time_entry = make_label_entry("Time (minutes)")
    mood_entry = make_label_entry("Mood")

    Button(form_win, text="Submit Run", command=submit_run, bg="#8DE6C2", fg="#34324A", font=("Helvetica", 12), relief=FLAT).pack(pady=20)

def on_set_goal():
    goal_win = Toplevel(root)
    goal_win.title("Set Your Weekly Goal")
    goal_win.geometry("300x200")
    goal_win.configure(bg="#34324A")
    goal_win.resizable(False, False)

    Label(goal_win, text="Weekly Distance Goal (km)", fg="white", bg="#34324A").pack(pady=(10, 0))
    goal_entry = Entry(goal_win)
    goal_entry.pack(pady=5)

    def save_goal():
        distance = goal_entry.get()
        result = set_user_goal(distance)
        messagebox.showinfo("Result", result)
        goal_win.destroy()
        refresh_runs_table()  # Refresh the table after setting a new goal

    Button(goal_win, text="Save Goal", command=save_goal, bg="#8DE6C2", fg="#34324A", font=("Helvetica", 12), relief=FLAT).pack(pady=20)

# Function to refresh the runs table
def refresh_runs_table():
    # Clear existing items in the treeview
    for item in tree.get_children():
        tree.delete(item)
    
    # Fetch and display updated runs
    runs = fetch_runs()
    for run in runs:
        tree.insert("", "end", values=run)

# Main GUI Layout
main_frame = Frame(root, bg="#34324A", padx=20, pady=20)
main_frame.pack(fill=BOTH, expand=True)

welcome_label = Label(main_frame, text="Welcome to TrackTrace!\nName___", fg="#8DE6C2", bg="#34324A", font=("Helvetica", 16, "bold"))
welcome_label.pack(pady=(0, 20))

log_button = Button(main_frame, text="Log/ save new runs", font=("Helvetica", 13), height=2, relief=FLAT, bg="#8DE6C2", fg="#34324A", command=on_log_run)
log_button.pack(fill=X, pady=(0, 20))

features_frame = Frame(main_frame, bg="#34324A")
features_frame.pack()

# Feature Buttons
Button(features_frame, text="Motivational Quotes", font=("Helvetica", 12), height=3, width=17, bg="#FFD3AC", relief=FLAT).grid(row=0, column=0, padx=10, pady=10)
Button(features_frame, text="Goal Setter", font=("Helvetica", 12), height=3, width=17, bg="#FFD3AC", relief=FLAT, command=on_set_goal).grid(row=0, column=1, padx=10, pady=10)

# Create a frame for the runs table
table_frame = Frame(main_frame, bg="#34324A")
table_frame.pack(fill=BOTH, expand=True, pady=20)

# Create a treeview to display runs
columns = ("ID", "Name", "Date", "Distance", "Time", "Mood", "Goal Met")
tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=8)

# Define column headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=60, anchor="center")

# Add a scrollbar
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

# Pack the tree and scrollbar
tree.pack(side="left", fill=BOTH, expand=True)
scrollbar.pack(side="right", fill="y")

# Fetch and display runs
refresh_runs_table()

bottom_frame = Frame(root, bg="white")
bottom_frame.pack(side=BOTTOM, fill=X)

Button(bottom_frame, text="🏠", font=("Helvetica", 10, "bold"), bg="#FFA15D", fg="white", relief=FLAT, padx=20, pady=10).pack(side=LEFT, expand=True)
Button(bottom_frame, text="START", font=("Helvetica", 10, "bold"), bg="#FFA15D", fg="white", relief=FLAT, padx=20, pady=10).pack(side=LEFT, expand=True)
Button(bottom_frame, text="⚙️", font=("Helvetica", 10, "bold"), bg="#FFA15D", fg="white", relief=FLAT, padx=20, pady=10).pack(side=LEFT, expand=True)

root.mainloop()