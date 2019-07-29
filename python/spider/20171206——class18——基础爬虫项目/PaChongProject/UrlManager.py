#coding:utf-8
#URL管理器

class UrlManager(object):

    #构造函数
    def __init__(self):
        # 创建一个set()集合存储没有被爬取的url
        self.new_urls=set()
        # 创建一个set()集合存储已经被爬取的url
        self.old_urls=set()

    def has_new_url(self):
        '''
        是否有没有爬取的url
        :return: 返回一个布尔类型的值，true:表示有，false:表示没有
        '''
        return self.new_urls_size()!=0

    def get_new_url(self):
        '''
        获取一个未被爬取的url,并从未被爬取的url集合中移除该url,
        并把该url添加到已被爬取的url集合中
        :return:
        '''
        #获取一个未被爬取的url,并从未被爬取的url集合中移除该url,
        url=self.new_urls.pop()
        #并把该url添加到已被爬取的url集合中
        self.old_urls.add(url)
        return url

    def add_new_url(self,url):
        '''
        给未被爬取的url集合中添加一个url
        :param url: 单个url
        :return:
        '''
        if url is None:
            return
        #判断已被抓取的url中和未被抓取的url中是否存在该url
        if url not in self.old_urls and url not in self.new_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        '''
        给未被爬取的url集合中添加多个url
        :param urls: 一个url集合
        :return:
        '''
        if urls is None:
            return
        for url in urls:
            self.add_new_url(url)


    def old_urls_size(self):
        '''
        返回已被爬取的url的个数
        :return:
        '''
        return len(self.old_urls)


    def new_urls_size(self):
        '''
        返回未被爬取的url的个数
        :return:
        '''
        return len(self.new_urls)




