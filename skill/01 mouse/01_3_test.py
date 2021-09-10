import pyautogui
'''
for i in range(1, 5):
    pyautogui.moveRel(100, 100, duration=0.5)
    pyautogui.moveRel(100, -100, duration=0.5)
    pyautogui.moveRel(-100, -100, duration=0.5)
    pyautogui.moveRel(-100, 100, duration=0.5)
    pyautogui.moveRel(100, 100, duration=0.5)

#read current position
x, y = pyautogui.position()
dx, dy = (100, 100)

#click
pyautogui.click()
pyautogui.click(x, y)
pyautogui.click(x, y, button='right')   # left, middle, right

pyautogui.doubleClick()
pyautogui.doubleClick(x, y)
pyautogui.middleClick()
pyautogui.middleClick(x, y)
pyautogui.rightClick()
pyautogui.rightClick(x, y)

pyautogui.dragTo(x, y, duration=0.25)
pyautogui.dragRel(dx, dy, duration=0.25)

pyautogui.mouseDown()
pyautogui.mouseDown(x, y, button='right')

pyautogui.mouseUp()
pyautogui.mouseUp(x, y, button='right')

pyautogui.scroll(100)   # scroll up
pyautogui.scroll(-100)  # scroll down


'''

pyautogui.moveRel(0, -20, duration=0.5)
#pyautogui.scroll(-100)
pyautogui.scroll(100)
#pyautogui.scroll(00, duration=1)
