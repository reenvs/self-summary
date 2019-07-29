#-*-coding:utf-8-*-
import requests
from lxml import etree
import re
import csv




def downloadHTML(url):
    user_agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0"
    headers={"User_Agent":user_agent}
    response=requests.get(url,headers=headers)
    response.encoding="utf-8"
    html_str=response.text
    return html_str

#解析器
def parseHTML(html_str):
    html=etree.HTML(html_str)
    div_mulus=html.xpath('//*[@class="mulu"]')
    rows=[]
    for mulu in div_mulus:
        h2=mulu.xpath("./div[@class='mulu-title']/center/h2")
        if len(h2)>0:
            h2_title=h2[0].xpath("./text()")
            h2title=h2_title[0].encode("utf-8")

            #获取章节的title,href,date
            a_s=mulu.xpath("./div[@class='box']/ul/li/a")
            for a in a_s:
                href=a.xpath("./@href")[0]
                title=a.xpath("./@title")[0]
                print href+"    "+title
                #数据清洗
                per=re.compile("\s*\[(.*)\]\s+(.*)\s*")
                match=per.search(title)
                date=match.group(1)
                real_title=match.group(2).encode("utf-8")
                rows.append((h2title,real_title,date,href))
    return rows


#存储器
def saveHTML(rows):
    header = ["书名","章节名", "时间", "连接"]
    with open("mulu.csv","w") as f:
        csv_f=csv.writer(f)
        csv_f.writerow(header)
        csv_f.writerows(rows)



html_str=downloadHTML("http://seputu.com/")
rows=parseHTML(html_str)
saveHTML(rows)
print rows