import pyautogui

im = pyautogui.screenshot()

color = im.getpixel((100, 100))  # (x, y)
print(color)

c2 = pyautogui.pixel(100, 100)
print(c2)

icon = im.crop((80, 400, 150, 500)) # left, top, right, bottom
icon.save('button1.png')
