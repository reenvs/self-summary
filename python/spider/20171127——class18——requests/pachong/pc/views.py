#-*-coding:utf-8-*-
from django.shortcuts import render
import requests
import bs4


# Create your views here.

def index(request):
    return render(request,"index.html")

#查询所有图片
def searchImg(request):
    #获取页面上传递的网址
    url=request.GET.get("url","")
    if url!="":
        response=requests.get(url)
        bsObject=bs4.BeautifulSoup(response.text)
        imgs=bsObject.find_all("img")
        #print imgs
        images_src=[]
        for img in imgs:
            print type(str(img))
            if img.attrs.get('data-src')!=None:
                print "data-src"+str(img.attrs.get('data-src'))
                images_src.append(str(img.attrs.get('data-src')))
            else:
                print "src:"+str(img.attrs.get('src'))
                images_src.append(str(img.attrs.get('src')))
        c={"images_src":images_src}
    return render(request,"showImages.html",c)
