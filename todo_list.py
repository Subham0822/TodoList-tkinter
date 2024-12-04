from tkinter import *
from tkinter import messagebox
from tkmacosx import Button  # Import Button from tkmacosx
from tkinter import PhotoImage

# Initialize main window
root = Tk()
root.geometry('666x466')
root.title('ToDo List')
root.iconphoto(True, PhotoImage(file='GUI/To-Do-tkinter/todo.png'))
root['bg'] = '#F5F5F5'  # Light pastel gray background

# Function to create a styled button
def makebt(text, cmd, bg, fg, hover_bg, hover_fg):
    return Button(
        root, 
        text=text, 
        command=cmd, 
        bg=bg, 
        fg=fg, 
        activebackground=hover_bg, 
        activeforeground=hover_fg, 
        font='ComicSansMS 12 bold', 
        borderless=1, 
        padx=12, 
        pady=8
    )

# Function to add text to list
def bt_add_press(event=None):
    e_text = e_input.get()  # Get the text from the entry widget
    if e_text.strip():  # Check if the text is not empty
        l_list.insert(END, e_text)  # Add the text to the listbox
        e_input.delete(0, END)  # Clear the entry widget

# Function to delete selected item
def bt_delete_press():
    try:
        selected = l_list.curselection()
        l_list.delete(selected)
    except TclError:
        pass

# Function to clear the list
def bt_clear_press():
    l_list.delete(0, END)

# Function to save list to file
def bt_save_press():
    text = l_list.get(0, END)
    with open('saved.txt', 'w') as f:
        for i in text:
            f.write(str(i) + '\n')
    messagebox.showinfo('Info', 'Saved Successfully!')

# Function to open list from file
def bt_open_press():
    try:
        with open('saved.txt', 'r') as f:
            l_list.delete(0, END)
            for line in f:
                l_list.insert(END, line.strip())
    except FileNotFoundError:
        messagebox.showerror('Error', 'File "saved.txt" not found in the directory.')

# ======== Labels ==========
l_title = Label(root, text='ToDo List', font='ComicSansMS 20 bold', bg='#F5F5F5', fg='#444')
l_title.place(x=250, y=10)

list_title = Label(root, text='Tasks:', font='ComicSansMS 14', bg='#F5F5F5', fg='#555')
list_title.place(x=10, y=50)

task_title = Label(root, text='New Task:', font='ComicSansMS 14', bg='#F5F5F5', fg='#555')
task_title.place(x=10, y=380)

# ======== Listbox ==========
l_list = Listbox(
    root, 
    width=55, 
    height=14, 
    font='ComicSansMS 13', 
    bg='#E7E7E7', 
    fg='#444', 
    selectbackground='#A6D1E6',  # Light blue for selected
    selectforeground='#000', 
    borderwidth=2, 
    highlightthickness=0
)
l_list.place(x=10, y=80)

# ======== Entry ==========
e_input = Entry(root, width=60, font='ComicSansMS 12', bd=2, bg='#FFFDD0', fg='#444')
e_input.place(x=10, y=410)
e_input.bind('<Return>', bt_add_press)  # Bind Enter key to the add function

# ======== Styled Buttons ==========
bt_delete = makebt('Delete', bt_delete_press, bg='#FF6961', fg='#FFF', hover_bg='#FF3B2F', hover_fg='#FFF')
bt_delete.place(x=525, y=80)

bt_clear = makebt('Clear', bt_clear_press, bg='#FFD700', fg='#444', hover_bg='#FFC107', hover_fg='#FFF')
bt_clear.place(x=525, y=130)

bt_save = makebt('Save', bt_save_press, bg='#77DD77', fg='#FFF', hover_bg='#44CC44', hover_fg='#FFF')
bt_save.place(x=525, y=180)

bt_open = makebt('Open', bt_open_press, bg='#779ECB', fg='#FFF', hover_bg='#4682B4', hover_fg='#FFF')
bt_open.place(x=525, y=230)

bt_add = makebt('Add', bt_add_press, bg='#FFB347', fg='#444', hover_bg='#FF914D', hover_fg='#FFF')
bt_add.place(x=525, y=403)

# Run the main loop
root.mainloop()
