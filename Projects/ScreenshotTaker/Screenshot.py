import pyscreenshot
from tkinter import *

root = Tk()
root.title("ScreenshotTaker")

num = 0
def takeScreenshot():
    image = pyscreenshot.grab()
    image.save("\\Screenshots Images\\screenshotname.png")
    image.show()
    
button = Button(root, text = "Take Screenshot", command = takeScreenshot)
button.grid(row=10, column=10)

root.mainloop()