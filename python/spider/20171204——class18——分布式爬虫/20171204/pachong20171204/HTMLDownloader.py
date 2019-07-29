#coding:utf-8
import requests
#HTML的下载器
class htmlDownloader(object):

    def download(self,url):
        '''
        通过url地址下载数据并返回
        :param url:
        :return:
        '''
        if url is None:
            return
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'}
        response=requests.get(url,headers=headers)
        response.encoding="utf-8"
        return response.text
