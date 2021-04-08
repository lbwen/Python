# coding: utf-8
import smtplib
from email.mime.text import MIMEText  # 发送纯文本邮件模板
from email.header import Header
from email.mime.multipart import MIMEMultipart

sender = 'hhm108@163.com'
receiver = '********@qq.com'  # 接收者
receivers = "************@qq.com"
subject = 'pythonemailtest77777'  # 主题
smtpserver = 'smtp.163.com'  # 发送邮件服务器
port = 25  # 端口
username = 'hhm108@163.com'  # 帐号
password = '************'  # 密码

body = 'rrrrrrrrrrr'  # 定义正文
# msg = MIMEText(body,'html','utf-8')#中文需参数‘utf-8'，单字节字符不需要
msg = MIMEMultipart()
msg['from'] = sender
# msg['to']=receiver
# msg['to']=";".join(receivers)
msg['to'] = receivers
msg['subject'] = subject

part = MIMEText("这是有附件的邮件")
msg.attach(part)

att = MIMEText(open('dis.html', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="dis.html"'
msg.attach(att)

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receivers, msg.as_string())
smtp.quit()

"""
#---这是附件部分--- 
#xlsx类型附件 
part = MIMEApplication(open('report.html','rb').read()) 
part.add_header('Content-Disposition', 'attachment', filename="report.html") 
msg.attach(part) 

#jpg类型附件 
part = MIMEApplication(open('22.jpg','rb').read()) 
part.add_header('Content-Disposition', 'attachment', filename="22.jpg") 
msg.attach(part) 

#pdf类型附件 
part = MIMEApplication(open('22.pdf','rb').read()) 
part.add_header('Content-Disposition', 'attachment', filename="22.pdf") 
msg.attach(part) 

#mp3类型附件 
part = MIMEApplication(open('22.mp3','rb').read()) 
part.add_header('Content-Disposition', 'attachment', filename="22.mp3") 
msg.attach(part) 

s = smtplib.SMTP("smtp.qq.com", timeout=30)#连接smtp邮件服务器,端口默认是25 
s.login(_user, _pwd)#登陆服务器 
s.sendmail(_user, _to, msg.as_string())#发送邮件 
s.close()
"""

