#coding:utf-8
import uniout
import unittest
import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText  # 发送纯文本邮件模板
from email.header import Header
from email.mime.multipart import MIMEMultipart
# from com.zrgk.demo5.Text import Tandao
def all_case():

    case_dir = r"D:\python\com\zrgk\demo5"     #测试目录
    testcase = unittest.TestSuite()   #单元测试
    discover = unittest.defaultTestLoader.discover(case_dir,pattern='Text*.py')
    #循环添加到测试套件中
    for test_suit in discover:
        for test_case in test_suit:
            #添加用例到testcase
            testcase.addTest(test_suit)
        # print testcase
        return  testcase
    # for x in discover:
    #     for y in x:
    #         testcase.addTest(x)
    # return testcase

def Mail():
    sender = '903292521@qq.com'
    receiver = '2629470244@qq.com'  # 接收者
    # receivers = "************@qq.com"
    subject = 'python测试邮件'  # 主题
    smtpserver = 'smtp.qq.com'  # 发送邮件服务器
    port = 465  # 端口
    username = '903292521@qq.com'  # 帐号
    # pad = 'msiznuyqrrxocaig'  # 密码
    pad = 'kyydanftagggbbbi'

    body = 'python邮件测试'  # 定义正文
    # msg = MIMEText(body,'html','utf-8')#中文需参数‘utf-8'，单字节字符不需要
    msg = MIMEMultipart()
    msg['from'] = sender
    # msg['to']=receiver
    # msg['to']=";".join(receivers)
    msg['to'] = receiver
    msg['subject'] = subject

    part = MIMEText(body, "This is html Test!", "utf-8")
    msg.attach(part)
    att = MIMEText(open('baogao.html', 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="baogao.html"'
    msg.attach(att)

    # 发送邮件
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.connect(smtpserver)
    smtp.login(username, pad)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    #返回实例
    report_path = "baogao.html"  #创建html
    # fg = file(report_path,'wb')
    fg = open(report_path,"w")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fg,title=u"报告",description="reort"
    )
    runner.run(all_case())
    Mail()

