import time

import pyautogui 

count = 5 
print('rady started go')

for i in range(count):
    print(count)
    time.sleep(1)
    count = count - 1

for i in range(10):
    pyautogui.typewrite ('Assalamu alaikum')
    pyautogui.press('enter')
    time.sleep(2)
