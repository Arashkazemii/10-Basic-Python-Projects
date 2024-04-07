import pyscreenshot
num = 0
def takeScreenshot():
    num+=1
    image = pyscreenshot.grab()
    image.save("\Screenshots Images\p%i"%num)