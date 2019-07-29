#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
from bs4.element import Comment
import student

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
soup2=BeautifulSoup(open("index.html"),"lxml")

print soup
print '-'*30
#提取文档中的title
print soup.title
print type(soup)
print type(soup.a)
print soup.title.name
print soup.a.attrs
soup.a.attrs['id']='aaa'#如果不存在key则抛出异常
del soup.a.attrs['id']
print soup.a.attrs
print soup.a.attrs.get('id')#如果不存在则返回None值
print soup.name
print soup.attrs
print '-'*50+"获取文本"+'-'*50
print type(soup.title.string)
print '-'*50+"获取注释"+'-'*50
if type(soup.a.string)==Comment:
    print "这是一个注释"
else:
    print type(soup.a.string)
print type(soup.title.string)

print soup.body.contents
print soup.body.children

for i in soup.body.children:
        print i
print "-"*50
print soup.body.descendants
for i in soup.body.descendants:
    print i
print "-"*50

print soup.head.string
print soup.title.string
print "-"*50
print soup.strings
for i in soup.stripped_strings:
    print i
print "-"*50
#获取一个元素在父元素
print soup.title.parent
#获取一个元素在祖先元素
print soup.title.parents
for i in soup.title.parents:
    print i


student=student.Student("zhangsan",25)
print student

print '-'*50+"获取兄弟节点"+'-'*50
print soup.p
print soup.p.next_sibling.next_sibling
print soup.p.prev_sibling
print '-'*50
for i in soup.p.next_siblings:
    print i


print '-'*50+"title前面的所有的元素"+'-'*50
print soup.title.previous_elements
for i in soup.title.previous_elements:
    print i
