'''
name_age = ["zhangsan","lisi","wangma",23,44,19]
print(name_age)
print(name_age[2].title())
print(name_age[-1])

message = "Your name is " + name_age[2] + "." 
print(message)

name_age[2] = 'wangwu'    #修改元素
print(name_age)
'''
""" #多行注释
name_age.append('xiaomin')  #添加元素
name_age.append(16)
print(name_age)

name_age.insert(2,'xiaohong') #插入元素
print(name_age)

del name_age[-1]                #删除元素
name = name_age.pop(-1)         #把删除元素存入一个新变量
print(name_age);print(name)
name_age.remove("xiaohong")     #不知道元素位置只知道元素值用remove
print(name_age)
"""

name_age = ["zhangsan","lisi","wangma",'jia','yl','bin']

print(sorted(name_age))    #sorted()按字母排序 临时排序
print(name_age)
name_age.sort()            #sort()给列表中的元素以开头字母来排序 永久排序
print(name_age)
name_age.reverse()         #把列表中的元素反转  永久排序
print(name_age)
print(len(name_age))