#coding:utf-8
#存储器
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class htmlSave(object):

    #定义一个构造函数
    def __init__(self):
        self.datas=[]

    #存储数据的函数
    def saveData(self,dicData):
        if dicData is not None:
            self.datas.append(dicData)

    def output(self):
        f=codecs.open("baike.html","w",encoding="utf-8")
        f.write("<html>")
        f.write("<body>")
        f.write("<table border='1'>")
        f.write("<tr><td>标题</td><td>简介</td><td>url</td></tr>")
        for data in self.datas:
            f.write("<tr>")
            f.write("<td width='100'>%s</td>"%data['title'])
            f.write("<td width='500'>%s</td>"%data['msg'])
            f.write("<td width='200'>%s</td>"%data['url'])
            f.write("</tr>")
        f.write("</table>")
        f.write("</body>")
        f.write("</html>")
