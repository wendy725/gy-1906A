# 字符串切片
# a= "赵娜真的很棒动作很慢步子很小"
# print(a[0:6])
# print(a[8:10])
# print(a[-2:])



#按照扑克牌的规则，现在有6张牌，只要5张
#黑桃（S）红桃（H）方块（D）梅花（C）
#牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
#数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
#[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]

a='''["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]'''
a=a[2:-2]

b=a.split('" , "')
print(b)
#
# a='1,2,3,4'

# a='''[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']'''
# print(a.replace("'",))
#





a='https://guoyasoft.com/login?redirect=%2Fdashboard'
xie=a.split('://')
print(xie)
xie=a.split('://')[0]
print(xie)

yu=a.split('://')[1]
print(yu)

yuy=yu[:yu.find('/')]
yut=yu[yu.find('/'):]
print(yuy)
print(yut)










