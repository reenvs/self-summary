#coding:utf-8
import hashlib
import cPickle

class URLManager(object):
    def __init__(self):
        #未读取的url
        self.new_urls=self.load_progress("new_urls.txt")
        #已读取的url
        self.old_urls=self.load_progress("old_urls.txt")


    def has_new_url(self):
        '''
        是否有未被读取的url
        :return:
        '''
        return self.new_urls_size()!=0

    def get_new_url(self):
        '''
        获取一个新的url
        :return:
        '''
        #从未被读取的url集合中取到一个新的url并从该集合中移除它
        new_url=self.new_urls.pop()
        m=hashlib.md5()
        m.update(new_url)
        old_url=m.hexdigest()[8:-8]
        self.old_urls.add(old_url)
        return new_url

    def add_new_url(self,url):
        '''
        添加一个新的url
        :return:
        '''
        if url is None:
            return
        m=hashlib.md5()
        m.update(url)
        if url not in self.new_urls and m.hexdigest()[8:-8] not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        '''
        添加多个url
        :return:
        '''
        if urls is None:
            return
        for url in urls:
            self.add_new_url(url)

    def old_urls_size(self):
        '''
        获取已抓取的url的个数
        :return:
        '''
        return len(self.old_urls)

    def new_urls_size(self):
        '''
        获取还没有抓取的url的个数
        :return:
        '''
        return len(self.new_urls)

    def save_progress(self,path,data):
        '''
        存储进度
        :param path:要保存数据的文件的地址
        :param data: 要保存的数据
        :return:
        '''
        with open(path,"wb") as f:
            cPickle.dump(data,f)


    def load_progress(self,path):
        '''
        从本地文件中加载数据
        :param path: 要加载的文件
        :return: 返回加载的数据
        '''
        try:
            with open(path,"rb") as f:
                t=cPickle.load(f)
                return t
        except:
            return set()