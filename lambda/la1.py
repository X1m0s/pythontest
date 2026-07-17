#python使用lambda创建函数，这是一种小型且匿名的内联函数，它可以具有任意数量的参数，但只能有一个表达式
#通常用于编写单行简单函数，在需要函数作为参数传递的情况下使用，例如map()、filter()、reduce()中
#lambda函数因为没有函数名称，所以只能通过赋值给变量或作为参数传递给其他函数来使用
#语法格式通常为: lambda arguments:expression
#lambda为定义函数的关键字，arguments为参数列表，可以包含零到多个函数，expresssion为函数主体的表达式

#这是一个无参lambda函数实例
f=lambda:"helloworld"
print(f())

#这是另外一个实例
x=lambda a:a+10
print(x(2))

#lambda函数也可以设置多个参数，参数使用逗号隔开
x=lambda a,b:a*b
print(x(5,6))

#lambda函数通常与内置函数map()、filter()和reduce()一起使用，以便在集合上执行操作
numbers=[1,2,3,4,5]
squared=list(map(lambda x:x**2,numbers))
print(squared)

#使用lambda函数与filter()一起，筛选偶数
numbers=[1,2,3,4,5,6,7,8]
even_numbers=list(filter(lambda x:x%2==0,numbers))
print(even_numbers)

#下面是一个使用reduce()和lambda表达式演示如何计算一个序列的累计乘积
from functools import reduce
numbers=[1,2,3,4,5]
product=reduce(lambda x,y:x*y,numbers)
print(product)
#上述实例中，reduce()函数通过遍历numbers列表，并使用lambda函数将累积的结果不断更新