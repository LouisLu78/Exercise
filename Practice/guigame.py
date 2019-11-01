# -*- conding:utf8 -*-
import pyautogui
from PIL import Image

pyautogui.PAUSE=1
pyautogui.FAILSAFE=True
print(pyautogui.size())

# for i in range(10):
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)

print(pyautogui.position())
pyautogui.scroll(200)
screen=pyautogui.screenshot()

screen.save('screen.PNG')
print(pyautogui.locateOnScreen('screen.PNG'))
print(pyautogui.locateOnScreen('yuna.PNG'))

import time
pyautogui.click(100,100)
pyautogui.typewrite('hello, I am a beginner for programming.')
time.sleep(1)
pyautogui.hotkey('alt', '3')