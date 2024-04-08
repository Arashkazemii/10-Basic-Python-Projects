# To-Do List App

This Python project allows users to create and manage a to-do list. It provides a simple GUI interface using the Tkinter library.

## Features

- Add tasks with descriptions and priorities.
- Display tasks with checkboxes indicating completion status.
- Mark tasks as completed or incomplete by double-clicking on them.
- Clear all tasks from the list.

## Requirements

- ```Python 3.x```
- ```Tkinter```

## How to Use

1. Run the Python script.
2. Enter the task description and priority in the respective fields.
3. Click the "Add Task" button to add the task to the list.
4. Double-click on a task to mark it as completed or incomplete.
5. Click the "Clear All Tasks" button to remove all tasks from the list.

## Sample Code

```python
import tkinter as tk

class Task:
    def init(self, description, priority):
        self.description = description
        self.priority = priority
        self.completed = False

class ToDoListApp:
    def init(self, root):
        # Code for initializing the app

    def add_task(self):
        # Code for adding a task to the list

    def clear_tasks(self):
        # Code for clearing all tasks from the list

    def display_tasks(self):
        # Code for displaying tasks in the listbox

    def toggle_task_completion(self, event):
        # Code for toggling task completion status

def main():
    # Code for running the main application

if name == "main":
    main()