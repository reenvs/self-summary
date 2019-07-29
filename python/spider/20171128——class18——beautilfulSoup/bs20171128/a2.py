#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
from bs4.element import Comment
import student
import re

html = """
<html><head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
#创建BeautifulSoup对象
soup=BeautifulSoup(html,"lxml")
#直接传入字符串
ps=soup.find_all("a")
for p in ps:
    print p

print "--------------------------"

#传入正则表达式
ps=soup.find_all(re.compile("^b"))
for p in ps:
    print p

print "--------------------------"

#传入列表
ps=soup.find_all(['a','b'])
for p in ps:
    print p

print "--------------------------"

#传入True
ps=soup.find_all(True)
for p in ps:
    print p


print "--------------------------"
def fun1(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

#传入True
ps=soup.find_all(fun1)
for p in ps:
    print p


print "------------关键字搜索--------------"
ps=soup.find_all(href=re.compile("^http"),id="link1")
for p in ps:
    print p

print "------------关键字冲突搜索--------------"
ps=soup.find_all(class_="sister")
for p in ps:
    print p


print "------------文本过滤--------------"
ps=soup.find_all(text=['The Dormouse\'s story','Lacie'])
for p in ps:
    print p


print "------------limit--------------"
ps=soup.find_all("a",limit=1)
for p in ps:
    print p


print "------------recursive=False--------------"
ps=soup.body.find_all("a",recursive=False)
for p in ps:
    print p


print "------------使用css选择器--------------"
ps=soup.select("p")
for p in ps:
    print p
