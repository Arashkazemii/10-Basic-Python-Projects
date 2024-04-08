import time

# Countdown Function
def countdown(t):
    while t:
        minutes, seconds = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds) 
        print(timer)
        time.sleep(1)
        t-=1
    
# Input in seconds
t = int(input('Enter Time Countdown :  '))
countdown(t)