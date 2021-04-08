#coding:utf-8
import ConfigParser
class ReadIni:
    def __init__(self,file_path = None):           #file_path：文件路径
        if file_path == None:
            self.file_path = "E:\python\word\Practice\Element.ini"
        else:
            self.file_path = file_path
        self.date = self.read_ini()

    def read_ini(self):
        read_ini = ConfigParser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini

    # def get_value(self,key):
    #     value = self.date.get("login_element",key)
    #     return value

#通过key获取对应的value
    def get_value(self,key,section=None):
        if section == None:
            section = "login_element"
        try:
            value =  self.date.get(section, key)
        except:
            value = None
        return value

if __name__ == '__main__':
    read = ReadIni()
    print read.get_value("register")