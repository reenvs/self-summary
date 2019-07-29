#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr



def _format_addr(s):
    name,addr = parseaddr (s)
    print formataddr ((Header (name,'utf-8' ).encode(),addr))
    return formataddr ((Header (name,'utf-8' ).encode(),addr))


#创建发送的信息对象
message=MIMEText("最近还好吗？","plain","utf-8")
#信息中添加发送者
message['Subject']=Header("问候","utf-8")
message[ 'From']=_format_addr ('一号爬虫<hqhx2017@163.com>')
message[ 'To']=_format_addr( '管理员<343627649@qq.com>')



smtp=smtplib.SMTP()
smtp.connect("smtp.163.com",25)
smtp.login("hqhx2017@163.com","hqhx123456")
smtp.sendmail("hqhx2017@163.com",["343627649@qq.com","838206775@qq.com"],message.as_string())
