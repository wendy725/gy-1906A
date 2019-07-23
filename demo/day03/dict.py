
#字典的特性：
#1 字典中的key是唯一的 不允许同一个键出现两次，创建是如果同一个键被赋值两次，后一个值会被记住
#2 key是不可改变的 数字，字符串，元组  元组(1,2,3,4)可以作为key，但是（1，[3]）不可以作为key
#3


#增
#创建
a= {}
#字典中新增一对数据
# a["姓名"]='小星星'
# print(a)

#改
# a["姓名"]='亮晶晶'
# print(a)

#删  pop参数只能为key
# a.pop("姓名")
# del a["姓名"]
# print(a)
# #清空字典
# a.clear()
# print(a)

#查
#根据key查看value
# print(a["姓名"])

#遍历字典（借助循环）
# for key in a:
#     print(a[key])

#字典合并
c={'姓名':'小新'}
d={'性别':'看心情'}
# c.update(d)
# print(c)
#两个字典合并，生成一个新字典
print(dict(c,**d))
print(c)
print(d)

#成员判断(姓名)
if("性别" in c):
    print("不存在字典中")
else:
    print("不存在字典中")