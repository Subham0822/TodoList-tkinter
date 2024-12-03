# ToDo List Application

A simple and user-friendly ToDo List application built using Tkinter in Python. This project showcases the use of Tkinter for GUI-based applications to manage daily tasks efficiently.

## Features
- Add Tasks: Quickly add tasks to the list.
- Delete Tasks: Remove selected tasks from the list.
- Clear All Tasks: Clear the entire task list with a single click.
- Save Tasks: Save the current list of tasks to a file.
- Open Tasks: Load previously saved tasks from a file.
- Keyboard Support: Press "Enter" to add tasks seamlessly.
- Interactive UI: A clean and visually appealing user interface with color-coded elements for better usability.

## Color Scheme
- Background: White (#FFFFFF).
- Text: Black (#000000).
- Task List Background: Cream (#FFFDD0).
- Input Field Background: Cream (#FFFDD0).
- Buttons:
  - Background: White (#FFFFFF).
  - Text: Black (#000000).

## Screenshot
[Click here]()

## Getting Started
### Prerequisites
- Python 3.x installed on your system.
## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/todolist-tkinter.git
2. Navigate to the project directory:
   ```bash
   cd todolist-tkinter
3. Run the Python script:
   ```bash
   python todo_list.py
   
## Usage
- Add Tasks: Enter the task in the input field and press "Enter" or click "Add".
- Delete Tasks: Select a task from the list and click "Delete".
- Clear All Tasks: Click "Clear" to remove all tasks from the list.
- Save Tasks: Click "Save" to save the tasks to a file named saved.txt.
- Open Tasks: Click "Open" to load tasks from the saved file.

## Project Structure
```bash
todo-list-tkinter/
│
├── todo_list.py       # Main Python script
├── saved.txt          # Task file (created when tasks are saved)
├── screenshot.png     # Sample screenshot
├── README.md          # Project documentation
└── .gitignore         # Git ignore file (if any sensitive files)
```
## How It Works
- Tasks are stored in a Listbox widget.
- The Save button writes all tasks to a text file, while the Open button loads tasks from a text file.
- The eval() function is not used for security purposes—string manipulation is done manually to ensure reliability.

## Contributing
Contributions are welcome! Feel free to submit a pull request or raise an issue for any suggestions or improvements.
