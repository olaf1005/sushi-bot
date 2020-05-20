#https://www.miniclip.com/games/sushi-go-round/en/

import pyautogui
import time
import botplay


items = pyautogui.locateOnScreen("images/_ordering.png", confidence = 0.9,grayscale = False)
print(items)
rice = (3*items[2]/4+items[0],items[3]/6+items[1])
nori = (items[2]/4+items[0],3*items[3]/6+items[1])
roe = (3*items[2]/4+items[0],3*items[3]/6+items[1])
phone =  pyautogui.locateOnScreen("images/phone.png", confidence = 0.9,grayscale = False)

# pyautogui.locateOnScreen("images/phone.png", confidence = 0.9,grayscale = False)

quantity = {'rice':10,'nori':10,'roe':10}

def onigiri_recipe():
	print("onigiri")
	for i in range(2):
		pyautogui.click(rice)
	pyautogui.click(nori)	
	pyautogui.click(pyautogui.locateCenterOnScreen("images/clear_mat.png",confidence = 0.7))

def california_recipe():
	print("California")
	pyautogui.click(rice)
	pyautogui.click(nori)
	pyautogui.click(roe)
	pyautogui.click(pyautogui.locateCenterOnScreen("images/clear_mat.png",confidence = 0.7))

def gunkan_maki_recipe():
	print("gunkan_maki")	
	pyautogui.click(rice)
	pyautogui.click(nori)
	for i in range(2):	
		pyautogui.click(roe)
	pyautogui.click(pyautogui.locateCenterOnScreen("images/clear_mat.png",confidence = 0.7))		

orders = []
order_count = 0


while True:
	if len(orders) <= order_count:
		onigiri_order = pyautogui.locateCenterOnScreen("images/onigiri_order.png",confidence = 0.7)
		california_roll_order = pyautogui.locateCenterOnScreen("images/california_roll_order.png",confidence = 0.7)
		gunkan_maki_order = pyautogui.locateCenterOnScreen("images/gunkan_maki_order.png",confidence = 0.7)
		if onigiri_order in orders:
			onigiri_order = None
		if california_roll_order in orders:
			california_roll_order = None
		if gunkan_maki_order in orders:
			gunkan_maki_order = None

		if order_count<6:
			if onigiri_order:
				if quantity['rice'] >=2 and quantity['nori'] >=1:	
					onigiri_recipe()
					orders.append(onigiri_order)
					quantity['rice'] -=2
					quantity['nori'] -=1
					order_count +=1
		if order_count<6:	
			if california_roll_order:
				if quantity['rice'] >=1 and quantity['nori'] >=1 and quantity['roe'] >=1:	
					california_recipe()
					orders.append(california_roll_order)
					quantity['rice'] -=1
					quantity['nori'] -=1
					quantity['roe'] -=1
					order_count +=1
		if order_count<6:	
			if gunkan_maki_order:
				if quantity['rice'] >=1 and quantity['nori'] >=1 and quantity['roe'] >=2:
					gunkan_maki_recipe()
					orders.append(gunkan_maki_order)
					quantity['rice'] -=1
					quantity['nori'] -=1
					quantity['roe'] -=2
					order_count +=1
	if (quantity['rice'] == 0):
		pyautogui.click(phone)
		riceordermenu = pyautogui.locateOnScreen("images/rice_order_menu.png", confidence = 0.9)
		pyautogui.click(riceordermenu)
		riceorderbutton = pyautogui.locateOnScreen("images/rice_order_button.png", confidence = 0.9)
		pyautogui.click(riceorderbutton)
		free = pyautogui.locateOnScreen("images/normal_delivery_button.png", confidence = 0.7,grayscale = False)
		pyautogui.click(free)
		quantity['rice'] = 10
		time.sleep(5)
	if (quantity['nori'] == 0):
		pyautogui.click(phone)
		toppingmenu = pyautogui.locateOnScreen("images/topping_order_menu.png", confidence = 0.9,grayscale = False)
		pyautogui.click(toppingmenu)
		noriorderbutton = pyautogui.locateOnScreen("images/nori_order_button.png", confidence = 0.9,grayscale = False)
		pyautogui.click(noriorderbutton)
		free = pyautogui.locateOnScreen("images/normal_delivery_button.png", confidence = 0.9,grayscale = False)
		pyautogui.click(free)
		quantity['nori'] = 10
		time.sleep(5)
	if (quantity['roe'] == 0):
		pyautogui.click(phone)
		toppingmenu = pyautogui.locateOnScreen("images/topping_order_menu.png", confidence = 0.9,grayscale = False)
		pyautogui.click(toppingmenu)
		roeorderbutton = pyautogui.locateOnScreen("images/roe_order_button.png", confidence = 0.9,grayscale = False)
		pyautogui.click(roeorderbutton)
		free = pyautogui.locateOnScreen("images/normal_delivery_button.png", confidence = 0.9,grayscale = False)
		pyautogui.click(free)
		quantity['roe'] = 10		
		time.sleep(5)

	plate = pyautogui.locateCenterOnScreen("images/pinkPlate.png",confidence = 0.5,grayscale = False)		
	if (plate):
		print("Pink Plate",plate)
		pyautogui.click(plate)
		min_dist = 999
		customer = None
		for i in orders:
			if min_dist > abs(i[0]-plate[0]):
				min_dist = abs(i[0]-plate[0])
				customer = i
		
		orders.remove(customer)
		if order_count>=0:
			order_count -=1
	print(orders)	
