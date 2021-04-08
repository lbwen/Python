#coding:utf-8
from AppiumPython.util.read_init import ReadIni
class GetByLocal:
    def __init__(self,driver):
        self.driver = driver
    def get_element(self,key):
        read_ini = ReadIni()
        local = read_ini.get_value(key)         #ReadIni，get_value获取ini文件中的value值
        #对ini文件进行拆分，判断是id/ClassName，以及定位信息
        if local != None:
            by = local.split(":")[0]
            local_by = local.split(":")[1]
            if by == "id":
                return self.driver.find_element_by_id(local_by)
            elif by == "className":
                return self.driver.find_element_by_class_name(local_by)
            else:
                return self.driver.find_element_by_xpath(local_by)
        else:
            return None

