#https://www.miniclip.com/games/sushi-go-round/en/

import pyautogui

def start():
	play= (pyautogui.locateCenterOnScreen("images/play_button.png",grayscale = False))
	if play:
		pyautogui.click(play)
		for i in range(2):
			conti= (pyautogui.locateCenterOnScreen("images/continue_button.png"))
			pyautogui.click(conti)

		skip= (pyautogui.locateCenterOnScreen("images/skip_button.png",grayscale = False))
		pyautogui.click(skip)

		conti= (pyautogui.locateCenterOnScreen("images/continue_button.png"))
		pyautogui.click(conti)
start()		