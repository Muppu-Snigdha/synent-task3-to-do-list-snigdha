from tkinter import *

# ---------------- MAIN WINDOW ---------------- #

root = Tk()

root.title("To-Do List")

root.geometry("1000x700")

root.configure(bg="#f8f6f2")

root.resizable(True, True)

# ---------------- TITLE ---------------- #

title = Label(

    root,

    text="To Do List",

    font=("Comic Sans MS", 34, "bold"),

    bg="#f8f6f2",

    fg="black"
)

title.pack(pady=20)

# ---------------- MAIN FRAME ---------------- #

main_frame = Frame(
    root,
    bg="#f8f6f2"
)

main_frame.pack(pady=10)

# ---------------- LEFT FRAME ---------------- #

left_frame = Frame(

    main_frame,

    bg="#f4d6d6",

    width=450,

    height=560
)

left_frame.grid(
    row=0,
    column=0,
    padx=25
)

left_frame.pack_propagate(False)

# ---------------- TODO TITLE ---------------- #

todo_title = Label(

    left_frame,

    text="To Do List",

    font=("Comic Sans MS", 26, "bold"),

    bg="#f4d6d6",

    fg="black"
)

todo_title.pack(pady=15)

# ---------------- ENTRY ---------------- #

task_entry = Entry(

    left_frame,

    font=("Poppins", 16),

    width=24,

    bg="white",

    fg="black",

    insertbackground="black",

    bd=0
)

task_entry.pack(
    pady=10,
    ipady=10
)

# ---------------- FUNCTIONS ---------------- #

def add_task():

    task = task_entry.get()

    if task != "":

        task_list.insert(END, "☐ " + task)

        task_entry.delete(0, END)


def delete_task():

    selected = task_list.curselection()

    if selected:

        task_list.delete(selected)


def clear_tasks():

    task_list.delete(0, END)

# ---------------- TASK LIST ---------------- #

task_list = Listbox(

    left_frame,

    font=("Poppins", 15),

    width=30,

    height=12,

    bg="#f4d6d6",

    fg="black",

    selectbackground="#d48b8b",

    bd=0,

    activestyle="none",

    highlightthickness=0
)

task_list.pack(pady=20)

# ---------------- BUTTON FRAME ---------------- #

button_frame = Frame(
    left_frame,
    bg="#f4d6d6"
)

button_frame.pack(pady=15)

# ---------------- BUTTON STYLE ---------------- #

button_style = {

    "font": ("Poppins", 12, "bold"),

    "fg": "white",

    "bd": 0,

    "cursor": "hand2",

    "padx": 15,

    "pady": 10
}

# ---------------- ADD BUTTON ---------------- #

add_button = Button(

    button_frame,

    text="ADD",

    bg="#6d8b74",

    activebackground="#6d8b74",

    command=add_task,

    **button_style
)

add_button.grid(
    row=0,
    column=0,
    padx=10
)

# ---------------- DELETE BUTTON ---------------- #

delete_button = Button(

    button_frame,

    text="DELETE",

    bg="#e07a5f",

    activebackground="#e07a5f",

    command=delete_task,

    **button_style
)

delete_button.grid(
    row=0,
    column=1,
    padx=10
)

# ---------------- CLEAR BUTTON ---------------- #

clear_button = Button(

    button_frame,

    text="CLEAR",

    bg="#3d405b",

    activebackground="#3d405b",

    command=clear_tasks,

    **button_style
)

clear_button.grid(
    row=0,
    column=2,
    padx=10
)

# ---------------- RIGHT FRAME ---------------- #

right_frame = Frame(
    main_frame,
    bg="#f8f6f2"
)

right_frame.grid(
    row=0,
    column=1,
    padx=10
)

# ---------------- NOTES FRAME ---------------- #

notes_frame = Frame(

    right_frame,

    bg="#f2b8a0",

    width=280,

    height=180,

    highlightbackground="white",

    highlightthickness=2
)

notes_frame.pack(
    pady=10
)

notes_frame.pack_propagate(False)

notes_title = Label(

    notes_frame,

    text="Notes",

    font=("Comic Sans MS", 24, "bold"),

    bg="#f2b8a0",

    fg="black"
)

notes_title.pack(pady=10)

notes_text = Text(

    notes_frame,

    font=("Poppins", 12),

    bg="#f2b8a0",

    fg="black",

    bd=0,

    height=5,

    width=24
)

notes_text.pack()

# ---------------- FOCUS FRAME ---------------- #

focus_frame = Frame(

    right_frame,

    bg="#b7d7d8",

    width=280,

    height=180,

    highlightbackground="white",

    highlightthickness=2
)

focus_frame.pack(
    pady=15
)

focus_frame.pack_propagate(False)

focus_title = Label(

    focus_frame,

    text="Focus",

    font=("Comic Sans MS", 24, "bold"),

    bg="#b7d7d8",

    fg="black"
)

focus_title.pack(pady=10)

focus_text = Text(

    focus_frame,

    font=("Poppins", 12),

    bg="#b7d7d8",

    fg="black",

    bd=0,

    height=5,

    width=24
)

focus_text.pack()

# ---------------- REMINDER FRAME ---------------- #

reminder_frame = Frame(

    right_frame,

    bg="#6d8b74",

    width=280,

    height=100
)

reminder_frame.pack(
    pady=10
)

reminder_frame.pack_propagate(False)

reminder_label = Label(

    reminder_frame,

    text="Remember ✨",

    font=("Comic Sans MS", 24, "bold"),

    bg="#6d8b74",

    fg="white"
)

reminder_label.pack(
    pady=25
)

# ---------------- FOOTER ---------------- #

footer = Label(

    root,

    text="Python Tkinter Aesthetic To-Do App",

    font=("Poppins", 11),

    bg="#f8f6f2",

    fg="gray"
)

footer.pack(
    pady=15
)

# ---------------- RUN APP ---------------- #

root.mainloop()