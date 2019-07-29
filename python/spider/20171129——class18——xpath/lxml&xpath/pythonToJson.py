#-*-coding:utf-8-*-
import json


obj=[{"sid":"s001","sname":"周静1","age":22},
{"sid":"s002","sname":"周静2","age":23},
{"sid":"s003","sname":"周静3","age":24},
{"sid":"s004","sname":"周静4","age":25}
]


#把python对象转成json对象
jsonObj=json.dumps(obj,skipkeys=True,ensure_ascii=False,indent=4)
print type(jsonObj)

with open("mulu.json","w") as f:
    json.dump(obj,fp=f,skipkeys=True,ensure_ascii=False,indent=4)

#把json字符串转成python对象
print type(jsonObj)
print type(json.loads(jsonObj))

with open("mulu.json","r") as f:
    print type(json.load(fp=f))
