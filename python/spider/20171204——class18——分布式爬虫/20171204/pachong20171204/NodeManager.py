#coding:utf-8
from multiprocessing import Process
from multiprocessing.managers import BaseManager
from multiprocessing import Queue
from URLManager import URLManager
from OutputFile import OutputFile

class NodeManager(object):

    def start_manager(self,url_q,result_q):
        # 把url_q,和result_q注册到网络上
        BaseManager.register('get_url_q',callable=lambda:url_q)
        BaseManager.register('get_result_q',callable=lambda:result_q)
        b=BaseManager(address=("192.168.32.130",8001),authkey="baike")
        return b


    def url_Manager_proc(self,url_q,conn_q,rootUrl):
	#创建一个url管理器
	urlManager=URLManager()
	#先把rootUrl添加到集合中去
	urlManager.add_new_url(rootUrl)
	while True:
		if urlManager.has_new_url():
			print "有"
			#获取一个未被爬去打url
			new_url=urlManager.get_new_url()
			print new_url
			#把要爬去的url地址放入url_q队列中，供给爬虫节点使用
			url_q.put(new_url)
		#判断当前爬去过的数据的条数
			if urlManager.old_urls_size()>2000:
				#如果已经爬取了2000个数据则给队列中存储over，用来通知爬虫节点，任务结束
				url_q.put("over")
				#把当前状态存储到文件中
				urlManager.save_progress("new_urls.txt",urlManager.new_urls)
				urlManager.save_progress("old_urls.txt",urlManager.old_urls)
				return
	
		#接收数据提取进程发送的关联的url
		if not conn_q.empty():
			a=conn_q.get()
			print a
			urlManager.add_new_urls(a)	


	#数据提取进程提取数据
    def result_solve_proc(self,result_q,conn_q,store_q):
        #假设解析器解析的数据是一个字典{"urls":urls,'datas':datas}
        if not result_q.empty():
            urls_datas=result_q.get()
            #提取关联的url
            urls=urls_datas['urls']     
            #提取数据
            datas=urls_datas['datas']
	    if urls=='over' and datas=='over':
		return
  	    #把提取的url添加到conn_q队列中
            conn_q.put(urls)
            #把提取的数据添加到store_q队列中
            store_q.put(datas)
			
    def save_data_proc(self,store_q):
	output=OutputFile()
	#把store_q队列中的数据存储到文件中
	if not store_q.empty():
		dic=store.get()
		output.store_data(dic)

						

if __name__=='__main__':
    url_q=Queue()#存储任务url
    result_q=Queue()#存储爬虫节点返回的结果
    conn_q=Queue()#存储当前页面关联的所有的url
    store_q=Queue()#存储当前页面的数据
    #创建一个分布式管理器
    node=NodeManager()
    m=node.start_manager(url_q,result_q)


    #创建第一个进程管理url地址
    urlManager_process=Process(target=node.url_Manager_proc,args=(url_q,conn_q,"http://baike.baidu.com/view/284853.html"));
    #创建一个进程,数据提取进程
    result_solve_process=Process(target=node.result_solve_proc,args=(result_q,conn_q,store_q))
    #创建一个进程,管理数据存储的
    save_data_process=Process(target=node.save_data_proc,args=(store_q,))
    #启动进程
    urlManager_process.start()
    result_solve_process.start()
    save_data_process.start()
    m.get_server().serve_forever()
