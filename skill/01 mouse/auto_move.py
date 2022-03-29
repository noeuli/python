import pyautogui
import time

fromX, fromY = pyautogui.position()
ten_min = 200
moveAmount = 100
hit_count = 0
dur = 3

print("Move mouse in 3 seconds")
time.sleep(3)

while True:
	moveAmount = moveAmount * (-1)
	print("move {0} for {1} seconds".format(moveAmount, dur))
	pyautogui.move(moveAmount, 0, dur) # move x+100 for a minute
	print("Click\n")
	hit_count = hit_count + 1
	pyautogui.click()
	wait_time = ten_min
	while wait_time > 0:
		print("wait {0} secs. hit {1} times".format(wait_time, hit_count))
		wait_time = wait_time - 1
		time.sleep(1)
