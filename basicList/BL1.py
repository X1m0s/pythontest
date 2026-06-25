#python中内置了6个序列的内置类型，最常见的是列表和元组
#列表都可以进行的操作包括索引、切片、加、乘、检查成员
#python同样内置了确定序列长度和确定最大最小的元素的方法
#列表的基础介绍在BDT3中，不再赘述
#更新列表时可以使用append()函数，下面是简单示例
list=["Google","Runoob",1997,2000]
print("第三个元素为:",list[2])
list[2]=2001
print("更新后的第三个元素为:",list[2])

list1=["Google","Runoob","Taobao"]
list1.append("Baidu")
print("更新后的列表:",list1)
#删除列表元素时可以使用del语句
list=["Google","Runoob",1997,2000]
print("原始列表:",list)
del list[2]
print("删除第三个元素后:",list)

#python列表脚本操作符如下所示
print(len([1,2,3]))                 #用于计算长度
print([1,2,3]+[4,5,6])              #用于组合两个列表
print(["Hi!"]*4)                    #用于重复
print(3 in [1,2,3])                 #用于判断元素是否存在于列表中
for x in [1,2,3]:print(x,end=" ")   #用于迭代

#嵌套列表的使用示例如下
list_a=["a","b","c"]
list_b=[1,2,3]
print("list_x=",list_x:=[list_a,list_b])
print("list_x[0]=",list_x[0],"list_x[0][1]=",list_x[0][1])

#列表比较是否相同需要引入operator模块的eq方法，示例如下
import operator
a=[1,2];b=[2,3];c=[2,3]
print("operator.eq(a,b):",operator.eq(a,b))
print("operator.eq(c,b):",operator.eq(c,b))