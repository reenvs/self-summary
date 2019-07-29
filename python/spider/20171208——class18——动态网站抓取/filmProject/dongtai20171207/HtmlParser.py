#coding:utf-8
from bs4 import BeautifulSoup
import re
import json

class HtmlParser(object):

    def parser_url(self,html_str):
        #从页面中解析出http://movie.mtime.com/70233/
        c=re.compile(r"(http://movie.mtime.com/(\d+)/)")
        urls=c.findall(html_str)
        if urls!=None:
            #去重
            return list(set(urls))
        else:
            return


    def parser_json(self,json_str):
        r=re.compile(r"=(.*?);")
        j=r.findall(json_str)
        json_strs=json.loads(j[0])

        b=json_strs.get('value').get('isRelease')
        if b:
            print "已经上映"
            self.parse_Release(json_strs)
        else:
            print "没有上映"
            self.parse_no_Release(json_strs)



    def parse_Release(self,json_strs):
        try:
            movieId=json_strs.get('value').get("movieRating").get("MovieId")
            userCount=json_strs.get('value').get("movieRating").get("Usercount")
            movieName=json_strs.get('value').get("movieTitle")
            TotalBoxOffice=json_strs.get('value').get("boxOffice").get("TotalBoxOffice")
            TotalBoxOfficeUnit=json_strs.get('value').get("boxOffice").get("TotalBoxOfficeUnit")
            print movieId, movieName, userCount, TotalBoxOffice + TotalBoxOfficeUnit
        except:
            print movieId, movieName,userCount


    def parse_no_Release(self,json_strs):
        movieId=json_strs.get('value').get("movieRating").get("MovieId")
        userCount=json_strs.get('value').get("movieRating").get("Usercount")
        movieName=json_strs.get('value').get("movieTitle")
        print movieId, movieName, userCount



