
# Countdown Timer

This project implements a simple countdown timer using the Tkinter library in Python, allowing the user to enter a specific time and count down to zero.

## Features

- Enter the desired time for countdown.
- Start, pause, and resume the countdown timer.
- Visual display of the countdown timer.

## How to Use

1. Copy the code and save it in a file with the .py extension.
2. Run the file.
3. Enter the desired time in the input field.
4. Click the "Start" button to begin the countdown.
5. Click the "Stop" button to stop the countdown.

## Sample Code

```python
import tkinter as tk
import time

def update_timer():
    global t
    if t > 0:
        minutes, seconds = divmod(t, 60)
        timer_label.config(text='{0:02d}:{1:02d}'.format(minutes, seconds), font=("Arial", 24, "bold"), foreground="black")
        t -= 1
        root.after(1000, update_timer)
    else:
        timer_label.config(text="Time's up!", font=("Arial", 24, "bold"), foreground="red")

def start_countdown():
    global t
    t = int(entry.get())
    update_timer()

def stop_countdown():
    global t
    t = 0

root = tk.Tk()
root.title("Countdown Timer")
root.geometry("400x200")
root.configure(background="#f0f0f0")  

label = tk.Label(root, text="Enter Number:", background="#f0f0f0", font=("Arial", 12, "bold"), foreground="black")
label.grid(row=0, column=0, pady=5, padx=5, sticky="nsew")

entry = tk.Entry(root, font=("Arial", 12, "bold"), bd=2, relief="solid")
entry.grid(row=0, column=1, pady=5, padx=5, sticky="nsew")

start_button = tk.Button(root, text="Start", command=start_countdown, font=("Arial", 12, "bold"), bg="#f0f0f0", fg="black", bd=2, relief="solid", padx=10, pady=5)
start_button.grid(row=1, column=0, pady=5, padx=5, sticky="nsew")

stop_button = tk.Button(root, text="Stop", command=stop_countdown, font=("Arial", 12, "bold"), bg="#f0f0f0", fg="black", bd=2, relief="solid", padx=10, pady=5)
stop_button.grid(row=1, column=1, pady=5, padx=5, sticky="nsew")

timer_label = tk.Label(root, text="", font=("Arial", 24, "bold"), background="#f0f0f0")
timer_label.grid(row=2, column=0, columnspan=2, pady=10, padx=5, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
