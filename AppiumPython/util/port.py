#coding:utf-8
from dos_cmd import DosCmd
class Port:
    def port_is_used(self,port_mun):
        '''
            判断端口是否被占用
        '''
        flag = None
        self.dos = DosCmd()
        command = "netstat -ano | findstr "+str(port_mun)
        result = self.dos.excute_cmd_result(command)
        if len(result)>0:
            flag = True
        else:
            flag = False
        return flag

    def create_post_list(self,start_post,device_list):
        '''
        生成可用端口
        @parameter start_pos
        @parameter device_list
        '''
        port_list = []
        if device_list != None:
            while len(port_list) != len(device_list):
                if self.port_is_used(start_post) != True:
                    port_list.append(start_post)
                start_post = start_post + 1
            return port_list
        else:
            print "生成端口失败"
            return None

if __name__ == '__main__':
    port = Port()
    li = [1,2,3,4,5]
    print port.create_post_list(4722,li)