#coding:utf-8
from read_ini import ReadIni

class ByLocal():
    def __init__(self,driver):
        self.driver = driver

    def get_element(self):
        read_ini = ReadIni()
        local = read_ini.get_value()        #ReadIni，get_value获取ini文件中的value值
        # 对ini文件进行拆分，判断是id/ClassName，以及定位信息
        if local != None:
            by = local.strip(":")[0]
            local_by = local.strip(":")[1]
            if by == "id":
                return self.driver.find_element_by_id(local_by)
            # elif by == "classname":
            #     return self.driver.find_element_by_classname(local_by)
            else:
                return self.driver.find_element_by_xpath(local_by)
        else:
            return None

# if __name__ == '__main__':
#     by = ByLocal()
#     print by.get_element()