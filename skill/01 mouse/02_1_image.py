import os
import pyautogui

file_path = os.path.dirname(__file__)
image_path = file_path + '/img/1.png'
print(image_path)

num1 = pyautogui.locateOnScreen(image_path)
print(num1)

num1pos = pyautogui.center(num1)
print(num1pos)

num1img = pyautogui.locateCenterOnScreen(image_path)
print(num1img)

imgList = list(pyautogui.locateAllOnScreen(image_path))
print(imgList)

