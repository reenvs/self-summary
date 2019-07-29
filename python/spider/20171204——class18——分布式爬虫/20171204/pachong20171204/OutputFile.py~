#coding:utf-8
import time
import codecs
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class OutputFile(object):
    #构造函数
    def __init__(self):
        self.filepath="%s.html"%(time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime()))
        self.output_head(self.filepath)
        self.datas=[]


    #存储数据
    def store_data(self,dic):
        if dic is None:
            return
        self.datas.append(dic)
        if len(self.datas)>10:
            self.output_body(self.datas)

    #输出文件头
    def output_head(self,filepath):
        f=codecs.open(filepath,"w",encoding="utf-8")
        f.write("<html>")
        f.write("<head>")
        f.write("<title>爬取百科数据</title>")
        f.write("</head>")
        f.write("<body>")
        f.write("<table>")
        f.write("<tr>")
        f.write("<td>标题</td><td>摘要</td><td>url地址</td>")
        f.write("</tr>")
        f.close()

    #输出文件主体
    def output_body(self,filepath):
        f=codecs.open(filepath,"a",encoding="utf-8")
        for data in self.datas:
            f.write("<tr>")
            f.write("<td>%d</td>"%data['title'])
            f.write("<td>%d</td>"%data['msg'])
            f.write("<td>%d</td>"%data['url'])
            f.write("</tr>")
            self.datas.remove(data)
        f.close()

    #输出文件尾
    def output_end(self,filepath):
        f=codecs.open(filepath,"w",encoding="utf-8")
        f.write("</table>")
        f.write("</body>")
        f.write("</html>")
        f.close()
