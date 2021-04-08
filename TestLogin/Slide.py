#coding:utf-8
import time
from appium import webdriver
class Slide:
    def get_driver(self):
        capabilities = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:21503",
            "app": "E:\word\shidonghui.apk",
            "appWaitActivity":"cn.com.open.mooc.index.splash.GuideActivity"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(10)
        return self.driver

    # 获取屏幕的宽高
    def get_size(self):
        self.size = self.driver.get_window_size()
        width = self.size['width']
        height = self.size['height']
        return width, height


    # 向左边滑动
    def swipe_left(self):
        # [100,200]
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x, y1, 2000)

    def swipe_on(self,direction):
        if direction == 'up':
            self.swipe_up()
        elif direction == 'down':
            self.swipe_down()
        elif direction == 'left':
            self.swipe_left()
        else:
            self.swipe_right()

if __name__ == '__main__':
    s= Slide()
    s.get_driver()
    s.swipe_on("left")