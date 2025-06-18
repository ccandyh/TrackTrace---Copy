from tkinter import *
from tkinter import ttk, messagebox
from main1 import *

root = Tk()
root.title("Fitness App")
root.geometry("400x600")

#functions
def on_log_run():
    name = name_entry.get()
    date = date_entry.get()
    distance = distance_entry.get()
    time = time_entry.get()
    goal = goal_entry.get()
    goal_met = goal_met_entry.get()
    mood = mood_entry.get()

    # Call the logic function from main1.py
    message = log_run(name, date, distance, time, goal, goal_met, mood)
    messagebox.showinfo("Run Logger", message)

def on_calorie_calc():
    calories = calculate_calories(30, intensity="high")  # Example input
    messagebox.showinfo("Calories Burned", f"Approx: {calories} calories in 30 mins")

def on_get_quote():
    quote = get_motivational_quote()
    messagebox.showinfo("Motivation", quote)

main_frame = Frame(root, padx=20, pady=20)
main_frame.pack(fill=BOTH, expand=True)

welcome_label = Label(main_frame, text="Welcome!")
welcome_label.pack(pady=(0, 20))

#Entry
name_frame = Frame(main_frame)
name_frame.pack(fill=X, pady=(0, 20))

name_label = Label(name_frame, text="Name")
name_label.pack(side=LEFT)

name_entry = Entry(name_frame, relief=SOLID, bd=1)
name_entry.pack(side=LEFT, fill=X, expand=True, padx=(10, 0))

date_label = Label(main_frame, text="Date")
date_label.pack()
date_entry = Entry(main_frame)
date_entry.pack(pady=5)

distance_label = Label(main_frame, text="Distance (km)")
distance_label.pack()
distance_entry = Entry(main_frame)
distance_entry.pack(pady=5)

time_label = Label(main_frame, text="Time (minutes)")
time_label.pack()
time_entry = Entry(main_frame)
time_entry.pack(pady=5)

goal_label = Label(main_frame, text="Goal (km)")
goal_label.pack()
goal_entry = Entry(main_frame)
goal_entry.pack(pady=5)

goal_met_label = Label(main_frame, text="Goal Met (Yes/No)")
goal_met_label.pack()
goal_met_entry = Entry(main_frame)
goal_met_entry.pack(pady=5)

mood_label = Label(main_frame, text="Mood")
mood_label.pack()
mood_entry = Entry(main_frame)
mood_entry.pack(pady=5)


#buttons
log_button = Button(main_frame, text="Log/ save new runs", height=2, relief=RIDGE, bd=2, bg="#4B4E6D", fg="white", command=on_log_run)
log_button.pack(fill=X, pady=(0, 10))

see_all_button = Button(main_frame, text="See all >", relief=FLAT, bd=0, fg="blue")
see_all_button.pack(side=RIGHT, fill=X, pady=(0, 20))

features_frame = Frame(main_frame)
features_frame.pack(fill=BOTH, expand=True)

calorie_button = Button(features_frame, text="Calorie calculator", height=2, relief=RAISED, bd=2, bg="#FFD3AC", command=on_calorie_calc)
calorie_button.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

goal_button = Button(features_frame, text="Goal setter", height=2, relief=RAISED, bd=2, bg="#FFD3AC")
goal_button.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

quotes_button = Button(features_frame, text="Motivational quotes", height=2, relief=RAISED, bd=2, bg="#FFD3AC", command=on_get_quote)
quotes_button.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

blog_button = Button(features_frame, text="Blog", height=2, relief=RAISED, bd=2, bg="#FFD3AC")
blog_button.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

start_button = Button(main_frame, text="START", height=2, relief=RAISED, bd=2, bg="#4B4E6D", fg="white")
start_button.pack(fill=X, pady=(20, 0))

root.mainloop()