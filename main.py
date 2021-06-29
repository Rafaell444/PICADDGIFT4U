#Simple Onclick SpamBot

import pyautogui
import time

for _ in range (30):#how many times needed to be written
    pyautogui.typewrite("YOU'VE BEEN HACKED")#message
    pyautogui.press("enter")#button press
    time.sleep(0.5) #time