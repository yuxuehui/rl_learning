#!/usr/bin/python
# -*- coding: UTF-8 -*-

me = "1043694812@qq.com"
dic = {"我自己": "1043694812@qq.com"}
user = 'loxs123@163.com'
password = 'GIOMYDFIFNGZFFUO'

import smtplib
from email.mime.text import MIMEText

from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart

import argparse
 
my_sender=user                  # 发件人邮箱账号
my_pass = password              # 发件人邮箱密码

my_user = dic.get("我自己")      # 收件人邮箱

def send_mail(title='--',text='----',file=None):
    ret=True
    try:
        # msg=MIMEText('刘畅你好','plain','utf-8')
        msg = MIMEMultipart()
        msg['From']=formataddr(["FromOut404",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["FK",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']=title                      # 邮件的主题，也可以说是标题
        
        body = text
        body = MIMEText(body) #将正文转换为MIME兼容字符串
        msg.attach(body)

        server=smtplib.SMTP_SSL("smtp.163.com")  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码


        # 常用文件附件
        if file is not None:
            zFile = file
            zApart = MIMEApplication(open(zFile, 'rb').read())
            zApart.add_header('Content-Disposition', 'attachment', filename=zFile.split("\\")[-1])

            msg.attach(zApart)

        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(e)
        ret=False
    return ret


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_name', default='PandaPickAndPlace-v3')
    args = parser.parse_args()

    ret=send_mail(file=args.file_name)
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
