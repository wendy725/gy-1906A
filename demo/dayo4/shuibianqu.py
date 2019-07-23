# [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
# a ='''["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]'''
# def ju_3_2(a):
#     a= a.replace("''",'"')
#     # print(a)
#     print(a[2:-2])
#     a=(a[2:-2])
#     # print(a)
#     b= a.split('" , "')
#     # print(b)
#     c={}
#     for i in b :
#         d=i[1:]
#         # print(d)
#         if(d in c):
#             c[d] += 1
#         else:
#             c[d] = 1
#     # print(c)
#     s1 = 0
#     s2 = 0
#     for key in c:
#         if(c[key] == 3):
#             s1 = 1
#         if(c[key] == 2 ) :
#             s2 = 1
#     if(s1==1 and s2 == 1):
#         print("三")
#     else:
#         print("不")
#
# with open("E:\\softwredata\\python\\gy_yy\\demo\\dayo4\\cards.txt",'r')as f:
#     z=f.readlines()
#     # print(z)
#     for v in z:
#         v=v.replace('\n','')
#         print(v)
#         ju_3_2(v)
#

def xj_cc(n,m):
    c=n*m
    print("结果",n,'*',m,'=',c)
    return c

def xj_ss(n,m):
    s=n+m
    print("结果",n,'+',m,'=',s)
    return s

def xj_jj(n,m):
    j=n-m
    print("结果",n,'-',m,'=',j)
#
def xj_vv(n,m):
    if(m !=0):
        v=n/m
        print("结果",n,'/',m,'=',v)
    else:
        print('除数不能为零')

# with open("E:\softwredata\python\gy_yy\demo\dayo4\cards.txt",'r')as f:

xj_ss(5,6)
xj_ss(xj_ss(5,6),7)


def bb(mx,yy,haoduo):
    return '{}欠{}{}命'.format(mx,yy,haoduo)
print(bb("罗明星","月月",'一条'))




def buy_coffees(cash=100,cups=1):
    #去咖啡店
    print("去咖啡店")
    #告诉服务员要几杯咖啡
    cup_num = cups
    print("告诉服务员要",cup_num,"杯咖啡")
    #服务员告诉你要多少钱
    print("服务员告诉你要",cup_num*30,"钱")
    #你给服务员多少钱
    money = cash
    print("你给服务员",money,"钱")
    #服务员找零，给你咖啡
    print("服务员找零",money-cup_num*30,"，给你",cup_num,"杯咖啡")

buy_coffees()
buy_coffees(200,5)

