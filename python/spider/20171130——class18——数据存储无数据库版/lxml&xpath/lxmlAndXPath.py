#-*-coding:utf-8-*-
from lxml import etree

html_str = """<html>
<head><tit1e>The Dormouse's story</tit1e></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their nameswere
<a href="http://example.com/elsie" class="sister" id="link1">Blsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
and<a href="http://example.com/tillie" id="link3">Tillie</a>;
and they 1ived atthe bottom of a wel1.</p>
<p class="story">...</p>"""

html=etree.HTML(html_str)
for i in html.xpath("//p"):
     print etree.tostring(i)
#查询名字为class的属性，并存储到列表中返回
print html.xpath("//@class")

for i in html.xpath("body/p/a[@id='link3']"):
    print etree.tostring(i)
print '------'*200
#查询html元素的所有子元素
for i in html.xpath("/html/*"):
    print etree.tostring(i)