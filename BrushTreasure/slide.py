#coding=utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
class Slide:
    def get_driver(self):
        capabilities = {
            "platformName": "Android",
            #"automationName":"UiAutomator2",
            "deviceName": "127.0.0.1:21503",
            "app": "E:\\apk\\shuabao.apk",
            "appWaitActivity":"com.jm.video.ui.main.MainActivity",
            "noReset":"true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)
        time.sleep(10)
        return self.driver

#获取屏幕的宽高
    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width,height

#向左边滑动
    def swipe_left(self):
        #[100,200]
        x1 = self.get_size()[0]/10*9
        y1 = self.get_size()[1]/2
        x = self.get_size()[0]/10
        self.driver.swipe(x1,y1,x,y1,2000)

#向右边滑动
    def swipe_right(self):
        #[100,200]
        x1 = self.get_size()[0]/10
        y1 = self.get_size()[1]/2
        x = self.get_size()[0]/10*9
        self.driver.swipe(x1,y1,x,y1,2000)

#向上滑动.
    def swipe_up(self):
        #[100,200]direction
        x1 = self.get_size()[0]/2
        y1 = self.get_size()[1]/10*9
        y = self.get_size()[1]/10
        self.driver.swipe(x1,y1,x1,y,1000)

#向下滑动
    def swipe_down(self):
        #[100,200]
        x1 = self.get_size()[0]/2
        y1 = self.get_size()[1]/10
        y = self.get_size()[1]/10*9
        self.driver.swipe(x1,y1,x1,y)

    def swipe_on(direction):
        if direction == 'up':
            Slide.swipe_up()
        elif direction == 'down':
            Slide.swipe_down()
        elif direction == 'left':
            Slide.swipe_left()
        else:
            Slide.swipe_right()

if __name__ == '__main__':
    Slide.get_driver()
    for i in range(1000):
        time.sleep(random.randint(2, 17))
        Slide.swipe_on("up")



