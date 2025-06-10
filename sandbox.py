from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Fitness App")
root.geometry("400x600")

# Main frame
main_frame = Frame(root, padx=20, pady=20)
main_frame.pack(fill=BOTH, expand=True)

# Welcome 
welcome_label = Label(main_frame, text="Welcome!")
welcome_label.pack(pady=(0, 20))

start_button = Button(main_frame, text="START", height=2, bg="#000080", fg="white", relief=RAISED, bd=2)
start_button.pack(fill=X, pady=(20, 0))

root.mainloop()
