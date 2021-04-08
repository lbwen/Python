#coding:utf-8
import smtplib
from email.mime.text import MIMEText  # 发送纯文本邮件模板
from email.header import Header
from email.mime.multipart import MIMEMultipart
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