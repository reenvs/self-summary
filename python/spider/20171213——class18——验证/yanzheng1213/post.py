import requests
from bs4 import BeautifulSoup

session=requests.session()
headers={"User_Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}
response=session.get("http://127.0.0.1:8000/loginInput",headers=headers)
loginhtml=response.text
# print loginhtml
soup=BeautifulSoup(loginhtml,"lxml");
csrf=soup.find(type="hidden")
csrfvalue=csrf.attrs.get("value")
print csrfvalue
postdata={"username":"zhangsan","password":"123456","csrfmiddlewaretoken":csrfvalue}
response=session.post("http://127.0.0.1:8000/login",data=postdata,headers=headers)
print response.text