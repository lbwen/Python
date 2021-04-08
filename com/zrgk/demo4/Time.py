#coding:utf-8
from selenium import webdriver
import time
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
d=webdriver.Firefox()
d.get("https://www.baidu.com/")
d.implicitly_wait(50)#隐式等待
#d.find_element_by_id("kw").send_keys("apple")
# element=WebDriverWait(d,10,0.5).until(EC.presence_of_element_located(d.find_element_by_id("kw")))
#显式等待
locators=("id","kw")
element=WebDriverWait(d,10,1).until(EC.presence_of_element_located(locator=locators))
elements=WebDriverWait(d,10,1).until_not(EC.title_is)

print type(element)
#(id ,"kw")
# WebDriverWait(d,10,0.5).until()
#WebDriverWait(driver, 超时时长, 调用频率, 忽略异常).until(可执行方法, 超时时返回的信息)
# driver：浏览器驱动
# timeout：最长超时等待时间
# poll_frequency：检测的时间间隔，默认为500ms
# ignore_exception：超时后抛出的异常信息，默认情况下抛 NoSuchElementException 异常
# 配合使用的 until() 或者 until_not() 方法说明：
# until(method, message='')
# 调用该方法体提供的回调函数作为一个参数，直到返回值为True
# until_not(method, message='')
# 调用该方法体提供的回调函数作为一个参数，直到返回值为False
# title_is：判断当前页面的title是否等于预期
# title_contains：判断当前页面的title是否包含预期字符串
# presence_of_element_located：判断某个元素是否被加到了dom树里，并不代表该元素一定可见
# visibility_of_element_located：判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0
# visibility_of：跟上面的方法做一样的事情，只是上面的方法要传入locator，这个方法直接传定位到的element就好了
# presence_of_all_elements_located：判断是否至少有1个元素存在于dom树中。举个例子，如果页面上有n个元素的class都是'column-md-3'，那么只要有1个元素存在，这个方法就返回True
# text_to_be_present_in_element：判断某个元素中的text是否 包含 了预期的字符串
# text_to_be_present_in_element_value：判断某个元素中的value属性是否包含了预期的字符串
# frame_to_be_available_and_switch_to_it：判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
# invisibility_of_element_located：判断某个元素中是否不存在于dom树或不可见
# element_to_be_clickable - it is Displayed and Enabled：判断某个元素中是否可见并且是enable的，这样的话才叫clickable
# staleness_of：等某个元素从dom树中移除，注意，这个方法也是返回True或False
# element_to_be_selected：判断某个元素是否被选中了,一般用在下拉列表
# element_located_to_be_selected
# element_selection_state_to_be：判断某个元素的选中状态是否符合预期
# element_located_selection_state_to_be：跟上面的方法作用一样，只是上面的方法传入定位到的element，而这个方法传入locator
# alert_is_present：判断页面上是否存在alert=

########################################
# 以下两个条件类验证title，验证传入的参数title是否等于或包含于driver.title
# title_is
# title_contains
# 以下两个条件验证元素是否出现，传入的参数都是元组类型的locator，如(By.ID, ‘kw’)
# 顾名思义，一个只要一个符合条件的元素加载出来就通过；另一个必须所有符合条件的元素都加载出来才行
# presence_of_element_located
# presence_of_all_elements_located
# 以下三个条件验证元素是否可见，前两个传入参数是元组类型的locator，第三个传入WebElement
# 第一个和第三个其实质是一样的
# visibility_of_element_located
# invisibility_of_element_located
# visibility_of
# 以下两个条件判断某段文本是否出现在某元素中，一个判断元素的text，一个判断元素的value
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# 以下条件判断frame是否可切入，可传入locator元组或者直接传入定位方式：id、name、index或WebElement
# frame_to_be_available_and_switch_to_it
# 以下条件判断是否有alert出现
# alert_is_present
# 以下条件判断元素是否可点击，传入locator
# element_to_be_clickable
# 以下四个条件判断元素是否被选中，第一个条件传入WebElement对象，第二个传入locator元组
# 第三个传入WebElement对象以及状态，相等返回True，否则返回False
# 第四个传入locator以及状态，相等返回True，否则返回False
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# 最后一个条件判断一个元素是否仍在DOM中，传入WebElement对象，可以判断页面是否刷新了
# staleness_of