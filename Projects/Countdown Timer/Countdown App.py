import tkinter as tk
import time

def update_timer():
    global t
    if t > 0:
        minutes, seconds = divmod(t, 60)
        timer_label.config(text='{0:02d}:{1:02d}'.format(minutes, seconds))
        t -= 1
        root.after(1000, update_timer)
    else:
        timer_label.config(text="Time's up!")

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

label = tk.Label(root, text="Enter Number:")
label.pack()

entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="Start Countdown", command=start_countdown)
start_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_countdown)
stop_button.pack()

timer_label = tk.Label(root, text="", font=("Helvetica", 48))
timer_label.pack()

root.mainloop()