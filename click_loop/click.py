import pyautogui
import datetime
import schedule
import time
import random

def job():

    x = random.uniform(0, 500)
    y = random.uniform(0, 500)
    dt_now = datetime.datetime.now()
    
    print(dt_now)
    print("click!!")
    pyautogui.moveTo(x, y, 1)
    #pyautogui.click(50, 100, 1, 0.5, 'left')
        
schedule.every(1/60).minutes.do(job)

while True:
    schedule.run_pending()
    #time.sleep(1)

