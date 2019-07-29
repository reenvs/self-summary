#coding:utf-8
import requests

class HtmlDownloader(object):

    def download(self,url):
        headers={"user_agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"}
        response=requests.get(url,headers=headers)
        response.encoding="utf-8"
        return response.text

