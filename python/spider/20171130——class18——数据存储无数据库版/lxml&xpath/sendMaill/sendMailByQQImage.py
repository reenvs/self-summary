# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def _format_addr(s):
    name, addr = parseaddr(s)
    print formataddr((Header(name, 'utf-8').encode(), addr))
    return formataddr((Header(name, 'utf-8').encode(), addr))

msgRoot = MIMEMultipart('related')
# 创建发送的信息对象
message = MIMEText('''
<html>
<body>
<h1 align='center'>图片</h1>
第一张图片：<img src='cid:image1' />
第二张图片：<img src='cid:image2' />
</body>
</html>
''', "html", "utf-8")
fp = open('../images/22b4815e-d57e-11e7-91bc-40f02f05b512.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

fp2 = open('../images/22c7942e-d57e-11e7-839a-40f02f05b512.jpg', 'rb')
msgImage2 = MIMEImage(fp2.read())
fp2.close()


#给图片指定一个id
msgImage.add_header('Content-ID', '<image1>')
msgImage2.add_header('Content-ID', '<image2>')

#把文本和图片都添加到msgRoot对象中
msgRoot.attach(message)
msgRoot.attach(msgImage)
msgRoot.attach(msgImage2)


# 信息中添加发送者
msgRoot['Subject'] = Header("问候", "utf-8")
msgRoot['From'] = _format_addr('一号爬虫<838206775@qq.com>')
msgRoot['To'] = _format_addr('管理员<343627649@qq.com>')

smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com", 25)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
smtp.set_debuglevel(1)
smtp.login("838206775@qq.com", "jfntntsqfchgbeab")
smtp.sendmail("838206775@qq.com", ["343627649@qq.com", "hqhx2017@163.com"], msgRoot.as_string())
