#在python中，使用了yield的函数成为生成器(generator)
#yield是用于定义生成器函数，生成器函数是一种特殊的函数，可在迭代过程中逐步产生值，而不是一次返回结果
#和普通函数不同的是，生成器的返回值是迭代器，只能用于迭代操作
#当生成器函数中使用yield语句时，函数执行将会暂停，并将yield后面的表达式作为当前迭代的值返回
#每次调用生成器的next()方法或使用for循环迭代时，函数会从上次暂停的地方继续执行，直到再遇到yield语句
#这样生成器函数可以逐步产生值，而不需要一次性计算并返回所有结果
#下面是一个展示生成器函数的使用的示例

def countdown(n):
    while n>0:
        yield n
        n-=1
#创建生成器对象
generator=countdown(5)
#通过迭代生成器获取值
print(next(generator))
print(next(generator))
print(next(generator))
#使用for循环迭代生成器
for value in generator:
    print(value)
#以上示例中，countdown函数是一个生成器函数，它使用yield语句逐步产生从n到1的倒数数字
#每次调用yield语句时，函数会返回当前的倒数值，并在下一次调用时从上次暂停的地方继续执行
#通过创建生成器对象并使用next()函数或for循环迭代生成器，我们可以逐步获取生成器函数产生的值
#在这个例子中，我们首先使用next()函数获取前三个倒数值，然后通过for循环获取剩下的两个倒数值
#生成器函数的优势是它们可以按需生成值，避免一次性生成大量数据并占用大量内存。
#此外，生成器还可以与其他迭代工具(如for循环)无缝配合使用，提供简洁和高效的迭代方式。

#以下示例使用yield实现斐波那契数列

import sys

def fibonacci(n):               #生成器函数
    a,b,counter=1,1,0
    while True:
        if (counter>n):
            return
        yield a
        a,b=b,a+b
        counter+=1
f=fibonacci(10)                 #f是一个迭代器，有生成器返回生成
while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()