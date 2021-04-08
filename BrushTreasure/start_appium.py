#coding=utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
def get_driver():
	capabilities = {
		"platformName": "Android",
		#"automationName":"UiAutomator2",
		"deviceName": "127.0.0.1:21503",
		"app": "E:\\apk\\shuabao.apk",
		"appWaitActivity":"com.jm.video.ui.main.MainActivity",
		"noReset":"true"
	}
	driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)
	time.sleep(10)
	return driver

#获取屏幕的宽高
def get_size():
	size = driver.get_window_size()
	width = size['width']
	height = size['height']
	return width,height

#向左边滑动
def swipe_left():
	#[100,200]
	x1 = get_size()[0]/10*9
	y1 = get_size()[1]/2
	x = get_size()[0]/10
	driver.swipe(x1,y1,x,y1,2000)

#向右边滑动
def swipe_right():
	#[100,200]
	x1 = get_size()[0]/10
	y1 = get_size()[1]/2
	x = get_size()[0]/10*9
	driver.swipe(x1,y1,x,y1,2000)

#向上滑动.
def swipe_up():
	#[100,200]direction
	x1 = get_size()[0]/2
	y1 = get_size()[1]/10*9
	y = get_size()[1]/10
	driver.swipe(x1,y1,x1,y,1000)

#向下滑动
def swipe_down():
	#[100,200]
	x1 = get_size()[0]/2
	y1 = get_size()[1]/10
	y = get_size()[1]/10*9
	driver.swipe(x1,y1,x1,y)

def swipe_on(direction):
	if direction == 'up':
		swipe_up()
	elif direction == 'down':
		swipe_down()
	elif direction == 'left':
		swipe_left()
	else:
		swipe_right()

driver = get_driver()
for i in range(1000):
	time.sleep(random.randint(2,17))
	swipe_on("up")
