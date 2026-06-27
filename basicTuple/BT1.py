#元组中只包含一个元素时，需要在元素后添加逗号,否则括号会被当作运算符使用
tup1=(50)
tup2=(50,)
print(type(tup1),type(tup2))
#元组不允许进行修改或删除，但可以使用连接符进行连接组合，或者使用del语句删除整个元组
tup1=(12,34.56)
tup2=("abc","xyz")
#tup1[0]=100            #非法运算
print(tup3:=tup1+tup2)  #合法运算
#del tup3[0]            #非法运算
del tup3                #合法运算，但已删除的元组再输出时报错
#元组同样支持部分运算符的使用，例如以下场景
print(len((1,2,3)))                 #计算元素个数
print((1,2,3)+(4,5,6))              #连接元组
print(("Hi!",)*4)                   #复制元组
print(3 in (1,2,3))                 #检查元组中是否存在元素
for x in (1,2,3):print(x,end=" ")   #迭代
#元组的不可变性指的是元组所指向的内存中的内容不可变，但地址映射的对象本身可以改变
#(比如将列表作为元素嵌入)
tup1=("R","U","N","O","O","B")
print("id(tup1)=",id(tup1))
tup1=(1,2,3,4,5,6)
print("id(tup1)=",id(tup1))
#从以上示例可以看出，为元组重新赋值之后，会绑定到新的对象，不是修改原来对象
#-----python内置元组操作函数-----
#与基础列表函数节内容大体一致，仅保留演示示例，不做过多文字描述
tuple1=("Google","Runoob","Taobao")
print(len(tuple1))
tuple1=("5","4","8")
print(max(tuple1),min(tuple1))
list1=["Google","Taobao","Runoob","Baidu"]
print(tuple(list1))