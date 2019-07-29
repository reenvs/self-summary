#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import re
import json


#下载器
def downloadHtml(url):
    user_agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:44.0) Gecko/20100101 Firefox/44.0"
    headers={"User_Agent":user_agent}
    response=requests.get(url,headers=headers)
    html_str=response.text
    response.encoding="utf-8"
    return html_str

#解析器
def parseHtml(html_str):
    soup=BeautifulSoup(html_str,"lxml")
    div_mulus=soup.find_all(class_='mulu')
    #存储
    books=[]
    for mulu in div_mulus:
    #从class=mulu的div中找h2元素
        h2=mulu.find("h2")
        if h2!=None:
            h2_title=h2.string.encode("utf-8")
            print h2_title
            # 查询所有章节的a超链接
            a_s= mulu.find(class_="box").find_all("a")
            chaps=[]
            for a in a_s:
                href=a.attrs.get("href")
                title=a.attrs.get("title")
                p=re.compile("\s*\[(.*)\]\s+(.*)\s*")
                match=p.search(title)
                date=match.group(1)
                real_title=match.group(2).encode("utf-8")
                d={"date":date,"real_title":real_title,"href":href}
                #print href + "     " + date+"    "+real_title
                chaps.append(d)

            #把所有的书存储到books
            books.append({"book_title":h2_title,"chapters":chaps})
            print books
            return books

#存储器
def saveHtml(books):
    with open("book.json","w") as f:
        json.dump(books, fp=f, skipkeys=True, ensure_ascii=False, indent=4)


html_str=downloadHtml("http://seputu.com/")
books=parseHtml(html_str)
saveHtml(books)
