import tkinter as tk  # Import Tkinter for creating GUI
from tkinter import ttk  # Import ttk for themed widgets
from tkinter import messagebox  # Import messagebox for displaying pop-up messages

# Function to add a new task
def add_task():
    task_string = task_field.get()  # Get the task string from the input field
    if len(task_string) == 0:  # Check if the input field is empty
        messagebox.showinfo('Error', 'Field is Empty.')  # Show error if empty
    else:
        tasks.append({"name": task_string, "status": "Incomplete"})  # Add the task with 'Incomplete' status
        list_update()  # Update the task list display
        task_field.delete(0, 'end')  # Clear the input field

# Function to update the task list display
def list_update():
    clear_list()  # Clear the listbox before updating
    for task in tasks:  # Insert each task into the listbox
        task_listbox.insert('end', f"{task['name']} - {task['status']}")  # Display task with its status

# Function to delete the selected task
def delete_task():
    try:
        selected_index = task_listbox.curselection()  # Get the index of the selected task
        if selected_index:
            task_listbox.delete(selected_index)  # Delete the selected task from the listbox
            tasks.pop(selected_index[0])  # Remove the task from the tasks list
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')  # Show error if no task is selected

# Function to mark a selected task as 'Complete'
def mark_complete():
    try:
        selected_index = task_listbox.curselection()  # Get the index of the selected task
        if selected_index:
            task = tasks[selected_index[0]]  # Get the task from the tasks list
            if task['status'] == 'Incomplete':  # Check if the task is incomplete
                task['status'] = 'Complete'  # Mark the task as complete
                list_update()  # Update the task list display
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Mark Complete.')  # Show error if no task is selected

# Function to delete all tasks from the list
def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  # Ask for confirmation before deleting all tasks
    if message_box:  # If the user confirms
        task_listbox.delete(0, 'end')  # Clear the listbox
        tasks.clear()  # Clear the tasks list

# Function to clear the task listbox
def clear_list():
    task_listbox.delete(0, 'end')  # Clear the listbox by deleting all its elements

# Function to close the GUI window
def close():
    guiWindow.destroy()  # Destroy the GUI window and exit the program

# Initialize the tasks list with some default tasks
tasks = [
    {"name": "Task 1", "status": "Incomplete"},
    {"name": "Task 2", "status": "Incomplete"},
    {"name": "Task 3", "status": "Incomplete"},
]

# Create the main window (GUI)
guiWindow = tk.Tk()
guiWindow.title("To-Do List")  # Set the title of the window
guiWindow.geometry("600x450+450+250")  # Set the window size and position
guiWindow.resizable(0, 0)  # Disable window resizing
guiWindow.configure(bg="#B0C4DE")  # Set the background color

# Create frames to organize the layout
header_frame = tk.Frame(guiWindow, bg="#B0C4DE")
functions_frame = tk.Frame(guiWindow, bg="#B0C4DE")
listbox_frame = tk.Frame(guiWindow, bg="#B0C4DE")

# Pack frames to the window
header_frame.pack(fill="both")
functions_frame.pack(side="left", expand=True, fill="both")
listbox_frame.pack(side="right", expand=True, fill="both")

# Create and pack the header label
header_label = ttk.Label(
    header_frame,
    text="To-Do List",
    font=("Harlow Solid Italic", "30"),
    background="#B0C4DE",
    foreground="#000000"
)
header_label.pack(padx=20, pady=20)

# Create and place the task input label and field
task_label = ttk.Label(
    functions_frame,
    text="Enter the Task:",
    font=("Times new roman", "18", "bold"),
    background="#B0C4DE",
    foreground="#000000"
)
task_label.place(x=30, y=10)

task_field = ttk.Entry(
    functions_frame,
    font=("Times new roman", "18"),
    width=18,
    background="#FFF8DC",
    foreground="#000000"
)
task_field.place(x=30, y=60)

# Create and place the buttons for Add, Delete, Mark Complete, and Exit
add_button = ttk.Button(
    functions_frame,
    text="Add Task",
    width=20,
    command=add_task  # Call the add_task function when clicked
)

del_button = ttk.Button(
    functions_frame,
    text="Delete Task",
    width=20,
    command=delete_task  # Call the delete_task function when clicked
)

mark_complete_button = ttk.Button(
    functions_frame,
    text="Mark Complete",
    width=20,
    command=mark_complete  # Call the mark_complete function when clicked
)

exit_button = ttk.Button(
    functions_frame,
    text="Exit",
    width=20,
    command=close  # Call the close function to exit the application
)

# Place the buttons at specific positions
add_button.place(x=75, y=150)
del_button.place(x=75, y=200)
mark_complete_button.place(x=75, y=250)
exit_button.place(x=75, y=300)

# Create and place the task listbox to display tasks
task_listbox = tk.Listbox(
    listbox_frame,
    width=25,
    height=12,
    font=("Times new roman", "15"),
    selectmode='SINGLE',
    background="#FFFFFF",
    foreground="#000000",
    selectbackground="#0000FF",
    selectforeground="#FFFFFF"
)
task_listbox.place(x=10, y=20)

# Update the listbox with tasks initially
list_update()

# Start the Tkinter event loop to run the GUI
guiWindow.mainloop()
