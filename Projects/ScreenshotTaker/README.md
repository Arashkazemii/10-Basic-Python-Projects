# Screenshot Taker

This Python project allows users to capture a screenshot of the current screen using the pyscreenshot library and display it.

## Features

- Capture a screenshot of the entire screen.
- Display the captured screenshot in a separate window.

## Requirements

- ```Python 3.x```
- ```Tkinter``` 
- ```Pyscreenshot``` 

## How to Use

1. Run the Python script.
2. Click the "Take Screenshot" button to capture a screenshot of the entire screen.
3. The captured screenshot will be displayed in a separate window.

## Sample Code

```python
import pyscreenshot
from tkinter import *

root = Tk()
root.title("ScreenshotTaker")

def takeScreenshot():
    image = pyscreenshot.grab()
    image.show()
    
button = Button(root, text="Take Screenshot", command=takeScreenshot)
button.grid(row=10, column=10)

root.mainloop()