from tkinter import *
from tkinter import messagebox
from tkmacosx import Button  # Import Button from tkmacosx
from tkinter import PhotoImage

# Initialize main window
root = Tk()
root.geometry('639x422')
root.title('ToDo List')
root.iconphoto(True, PhotoImage(file='GUI/To-Do-tkinter/todo.png'))
root['bg'] = '#fff'

# Function to create a styled button
def makebt(text, cmd):
    return Button(root, text=text, command=cmd, bg='#fff', fg='#000', font='ComicSansMS 12',
                  borderless=1, activebackground='#D3D3D3', activeforeground='#000', padx=10, pady=5)

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
    messagebox.showinfo('Info', 'Saved')

# Function to open list from file
def bt_open_press():
    try:
        with open('saved.txt', 'r') as f:
            l_list.delete(0, END)
            for line in f:
                l_list.insert(END, line.strip())
    except FileNotFoundError:
        messagebox.showerror('FileNotFound', 'File "saved.txt" not found in directory')

# ======== Labels ==========
l_title = Label(root, text='ToDo List', font='ComicSansMs 18', bg='#fff', fg='#000')
l_title.place(x=250, y=0)

list_title = Label(root, text='Tasks:', font='ComicSansMs 14', bg='#fff', fg='#000')
list_title.place(x=10, y=30)

list_title = Label(root, text='New Task:', font='ComicSansMs 14', bg='#fff', fg='#000')
list_title.place(x=10, y=340)

# ======== Listbox ==========
l_list = Listbox(root, width=55, height=14, font='ComicSansMs 13', bg='#FFFDD0', fg='#000',
                 selectbackground='#D3D3D3', selectforeground='#000')
l_list.place(x=10, y=60)

# ======== Entry ==========
e_input = Entry(root, width=55, font='ComicSansMs 12', bd=1, bg='#FFFDD0', fg='#000')
e_input.place(x=10, y=370)
e_input.bind('<Return>', bt_add_press)  # Bind Enter key to the add function

# ======== Styled Buttons ==========
bt_delete = makebt('Delete', bt_delete_press)
bt_delete.place(x=525, y=60)

bt_clear = makebt('Clear', bt_clear_press)
bt_clear.place(x=525, y=95)

bt_save = makebt('Save', bt_save_press)
bt_save.place(x=525, y=130)

bt_open = makebt('Open', bt_open_press)
bt_open.place(x=525, y=165)

bt_add = makebt('Add', bt_add_press)
bt_add.place(x=525, y=366)

# Run the main loop
root.mainloop()
