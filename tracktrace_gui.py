from tkinter import *
from tkinter import ttk, messagebox
from main1 import *

root = Tk()
root.title("Tidetrace: Running App")
root.geometry("400x750")
root.configure(bg="#34324A")

#functions
def on_log_run():
    #new window--
    form_win = Toplevel(root)
    form_win.title("Log a Run")
    form_win.geometry("350x500")
    form_win.configure(bg="#34324A")

    def submit_run():
        name = name_entry.get()
        date = date_entry.get()
        distance = distance_entry.get()
        time = time_entry.get()
        goal = goal_entry.get()
        goal_met = goal_met_entry.get()
        mood = mood_entry.get()

        message = log_run(name, date, distance, time, goal, goal_met, mood)
        messagebox.showinfo("Run Logger", message)
        form_win.destroy()

    def make_label_entry(text):
        Label(form_win, text=text, bg="#34324A", fg="white", anchor="w").pack(fill=X, padx=10)
        entry = Entry(form_win, relief=FLAT, bg="white")
        entry.pack(fill=X, padx=10, pady=(0, 10))
        return entry

    name_entry = make_label_entry("Name")
    date_entry = make_label_entry("Date")
    distance_entry = make_label_entry("Distance (km)")
    time_entry = make_label_entry("Time (minutes)")
    goal_entry = make_label_entry("Goal (km)")
    goal_met_entry = make_label_entry("Goal Met (Yes/No)")
    mood_entry = make_label_entry("Mood")

    Button(form_win, text="Submit Run", command=submit_run, bg="#8DE6C2", fg="#34324A", font=("Helvetica", 12), relief=FLAT).pack(pady=20)

def on_calorie_calc():
    calories = calculate_calories(30, intensity="high")
    messagebox.showinfo("Calories Burned", f"Approx: {calories} calories in 30 mins")

def on_get_quote():
    quote = get_motivational_quote()
    messagebox.showinfo("Motivation", quote)

main_frame = Frame(root, bg="#34324A", padx=20, pady=20)
main_frame.pack(fill=BOTH, expand=True)

welcome_label = Label(main_frame, text="Welcome!\nName___", fg="#8DE6C2", bg="#34324A", font=("Helvetica", 16, "bold"))
welcome_label.pack(pady=(0, 20))

#buttons
log_button = Button(main_frame, text="Log/ save new runs", font=("Helvetica", 13), height=2, relief=FLAT, bg="#8DE6C2", fg="#34324A", command=on_log_run)
log_button.pack(fill=X, pady=(0, 20))

#feature cards
features_frame = Frame(main_frame, bg="#34324A")
features_frame.pack()

Button(features_frame, text="Calorie Calculator", font=("Helvetica", 12), height=3, width=17, bg="#FFD3AC", relief=FLAT, command=on_calorie_calc).grid(row=0, column=0, padx=10, pady=10)
Button(features_frame, text="Goal Setter", font=("Helvetica", 12), height=3, width=17, bg="#FFD3AC", relief=FLAT).grid(row=0, column=1, padx=10, pady=10)
Button(features_frame, text="Motivational Quotes", font=("Helvetica", 12), height=3, width=17, bg="#FFD3AC", relief=FLAT, command=on_get_quote).grid(row=1, column=0, padx=10, pady=10)
Button(features_frame, text="Blog", font=("Helvetica", 12), height=3, width=17, bg="#FFD3AC", relief=FLAT).grid(row=1, column=1, padx=10, pady=10)

#bottom nav
bottom_frame = Frame(root, bg="white")
bottom_frame.pack(side=BOTTOM, fill=X)


#---todo: insert img
Button(bottom_frame, text="🏠", font=("Helvetica", 10, "bold"), bg="#FFA15D", fg="white", relief=FLAT, padx=20, pady=10).pack(side=LEFT, expand=True)
Button(bottom_frame, text="START", font=("Helvetica", 10, "bold"), bg="#FFA15D", fg="white", relief=FLAT, padx=20, pady=10).pack(side=LEFT, expand=True)
Button(bottom_frame, text="⚙️", font=("Helvetica", 10, "bold"), bg="#FFA15D", fg="white", relief=FLAT, padx=20, pady=10).pack(side=LEFT, expand=True)

root.mainloop()

