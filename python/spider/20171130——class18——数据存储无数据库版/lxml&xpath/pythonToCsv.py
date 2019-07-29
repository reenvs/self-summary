#-*-coding:utf-8-*-
import csv
from collections import namedtuple

headers=['ID','Username','Password','Age','Country']
rows=[
    (1001,'zhoujing','zhoujing_pass',24,'China'),
    (1002,'zhanglei','zhanglei_pass',20,'USA'),
    (1003,'zhaojing','zhaojing_pass',20,'USA'),
]


# with open("stu.csv","w") as f:
#     csv_f=csv.writer(f)
#     csv_f.writerow(headers)
#     csv_f.writerows(rows)
#     print type(csv_f)



#读取数据
with open("stu.csv","r") as f:
        # f_csv=csv.reader(f)

        #通过列表形式取值
        # print header[0] + " " + header[1] + " " + header[2]
        # for i in csv_f:
        #     print i[0]+" "+i[1]+" "+i[2]
        #通过命名元祖的方式
        # headings = next(f_csv)
        # Row = namedtuple("Row", headings)
        # print Row
        # for r in f_csv:
        #     row= Row(*r)
        #     print row.Username, row.Password,row.Age
        #     print row
        #使用字典的方式读取
        reader=csv.DictReader(f)
        for row in reader:
            print row.get("Username"),row.get("Age")