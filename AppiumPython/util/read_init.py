#coding:utf-8
import ConfigParser
# read_ini = ConfigParser.ConfigParser()
# read_ini.read("E:\python\word\AppiumPython\config\LocalElement.ini")
# print read_ini
# print read_ini.get("login_element","username")

class ReadIni:
    def __init__(self,file_path = None):
        if file_path == None:
            self.file_path = "E:\python\word\AppiumPython\config\LocalElement.ini"
        else:
            self.file_path = file_path
        self.date = self.read_ini()
    def read_ini(self):
        read_ini = ConfigParser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini

    #通过key获取对应的value
    def get_value(self,key,section=None):
        if section == None:
            section = "login_element"
        try:
            value = self.date.get(section, key)
        except:
            value = None
        return value

    # def get_value(self,key):
    #     return self.date.get("login_element",key)

if __name__ == '__main__':
    read_ini = ReadIni()
    print read_ini.get_value("username","login_element")