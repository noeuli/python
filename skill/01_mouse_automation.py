import pyautogui
import time

buttons = { '1': (40, 260), '2': (80, 260), '3':(110, 260), 'x':(100, 160)}

'''
x, y = buttons['x'] #버튼 3의 위치를 가져온다
pyautogui.moveTo(x, y, duration=0.5)
pyautogui.click()
x, y = buttons['2'] #버튼 3의 위치를 가져온다
pyautogui.moveTo(x, y, duration=0.5)
pyautogui.click()
x, y = buttons['1'] #버튼 3의 위치를 가져온다
pyautogui.moveTo(x, y, duration=0.5)
pyautogui.click()
#pyautogui.click(x, y)   #클릭한다.
'''

for c in 'x123':
    x, y = buttons[c]
    #pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click(x, y, duration=0.4)
