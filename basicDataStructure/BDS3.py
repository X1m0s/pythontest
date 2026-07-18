#列表推导式提供了从序列创建列表的简单途径，通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列
#每个列表推导式都在for之后跟一个表达式，然后有零到多个for或if自居，返回结果是一个根据表达从其后的for和if上下文环境中生成出来的列表
#下面开始是几个简单的小实例
vec=[2,4,6]
print([3*x for x in vec])
print([[x,x**2] for x in vec])
freshfruit=['  banana','  loganberry ','passion fruit  ']
print([weapon.strip() for weapon in freshfruit])
#可以使用if子句作为过滤器
print([3*x for x in vec if x>3])
print([3*x for x in vec if x<2])
#以下是一些关于循环和其他技巧的演示:
vec1=[2,4,6];vec2=[4,3,-9]
print([x*y for x in vec1 for y in vec2])
print([x+y for x in vec1 for y in vec2])
print([vec1[i]*vec2[i] for i in range(len(vec1))])
#列表推导式可以使用复杂表达式或嵌套函数:
print([str(round(355/113,i)) for i in range(1,6)])

#python的列表同样支持嵌套，下面的几个实例会简单介绍这一点
matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],      #这段的尾逗号是一种防御性写法，便于后期维护，此外git diff时加了逗号的版本只会显示新增行，代码审查时更清楚
]
print([[row[i] for row in matrix] for i in range(4)])       #将3*4矩阵转置为4*3矩阵
#也可以用下面这个方法实现
transposed=[]
for i in range(4):
    transposed.append([row[i] for row in matrix])
print("另一种计算方式:",transposed)
#还有一种实现方式
transposed=[]
for i in range(4):
    transposed_row=[]
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print("另另一种计算方式:",transposed)

#使用del语句可以从一个列表中根据索引来删除一个元素，而不是值来删除元素，这与使用pop()返回一个值不同
#可以用del语句从列表中删除一个切割，或清空整个列表，相关实例如下所示
a=[-1,1,66.25,333,333,1234.5]
del a[0];print(a)
del a[2:4];print(a)
del a[:];print(a)               #先前介绍的方法是给切割赋一个空列表，当然也可以用del直接删除变量

