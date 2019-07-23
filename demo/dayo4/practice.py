'''
# 按照扑克牌的规则，现在有6张牌，只要5张
# 黑桃（S）红桃（H）方块（D）梅花（C）
# 牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
# 数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
# [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
# '''
# a = '''[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']'''
# # ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
# #统一符号
# a=a.replace("''",'"')
# print(a)
# #去掉括号 截取
# a=a[2:-2]
# print(a)
# #切片
# c=a.split('" , "')
# print(c)
#
# # 第四步：取出后面的数字  循环遍历取出list里面的每个值，对这个值进行截取
# d={}
# for i in c:
#     j=i[1:]
#     print(j)
# # 第五步：统计相同的数字个数  用字典去统计
#     if (j not in d):
#         d[j]=1
#     else:
#         d[j]+=1
#     print(d)
#
# # 第六步：判断数据中有没有同时存在三个相同数字和两个相同数字  if判断
# # 如果key对应的数值有3的 v1 = 1，如果没有则为0
# # 如果key对应的数值有2的 v2 = 1，如果没有则为0
#
# for k in d:
#     if(d[k]==3):
#         v1=1
#     if(d[k]==2):
#         v2=1
#     if(v1==1 and v2==1):
#         print("三带二")
#     else:
#         print("什么鬼东西")

def ju_3_2(a):
# a ='''["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]'''
    # ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
    #统一符号
    a=a.replace("''",'"')
    # print(a)
        #去掉括号 截取
    a=a[2:-2]
        # print(a)
        #切片
    c=a.split('" , "')
        # print(c)
        # 第四步：取出后面的数字  循环遍历取出list里面的每个值，对这个值进行截取
    d={}
    for i in c:
        j=i[1:]
            # print(j)
        # 第五步：统计相同的数字个数  用字典去统计
        if (j not in d):
            d[j]=1
        else:
            d[j]+=1
            # print(d)
        # 第六步：判断数据中有没有同时存在三个相同数字和两个相同数字  if判断
        # 如果key对应的数值有3的 v1 = 1，如果没有则为0
        # 如果key对应的数值有2的 v2 = 1，如果没有则为0
        v1=0
        v2=0

        for key in d:
            if(d[key]==3):
                v1=1
            if(d[key]==2):
                v2=1
        if(v1==1 and v2==1):
            print("三带二")
        else:
            print("不玩了")
# for f in range (3):
#     ju_3_2()

with open("E:\\softwredata\\python\\gy_yy\\demo\\dayo4\\cards.txt",'r')as f:
    z=f.readlines()
    print(z)
    for x in z:
        c=x.replace('\n','')
        print(c)
        ju_3_2(c)