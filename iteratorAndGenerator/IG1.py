#迭代器(generator)是python中访问集合元素的一种方式，是一个可以记住遍历位置的对象
#迭代器对象从集合的第一个元素开始访问，直到所有元素访问完毕结束，迭代器只能向前不能后退
#迭代器有两个基础方法iter()和next()，字符串、列表或元组对象均可用于创建迭代器
#示例如下:
list1=[1,2,3,4]
it=iter(list1)
print(next(it),next(it),next(it),next(it))      #next不能访问超出边界的部分，会直接报错
print(type(it))                                 #<class 'list-generator'>
#迭代器对象可以使用常规for语句进行遍历:
list1=[1,2,3,4]
it=iter(list1)
for x in it:
    print(x,end=" ")
print()
#也可以正常使用next()进行遍历
# import sys
# list1=[1,2,3,4]
# it=iter(list1)
# while True:
#     try:
#         print(next(it),end=" ")
#     except StopIteration:
#         sys.exit()                              #尽量使用程序化退出,sys.exit()没有多余提示

#创建一个迭代器
#把类作为一个迭代器使用需要实现两个方法:__iter__()和__next__(),python的构造函数为__init()__
#__iter__()方法返回一个特殊的迭代器对象，对象实现了__next__()方法并通过StopIteration异常标识迭代的完成
#__next__()方法(python2中是next())会返回序列中下一个元素
#下面是创建返回数字的迭代器示例，初始值为1，递增1
class MyNumbers:
    def __iter__(self):
        self.a=1
        return self                     
    
    def __next__(self):
        x=self.a
        self.a+=1
        return x
#通常这里需要raise StopIteration,不写这部分内容也不会导致类直接报错，但用for时会无限循环

myclass=MyNumbers()   #创建一个MyNumber类对象，此时该对象还未转换为迭代器
myiter=iter(myclass)  #调用__iter__()，完成两件事:a初始化为1、返回self，让myiter和myclass指向同一对象
                      #一步到位的写法:myiter=iter(MyNumbers())
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#StopIteration异常用于标识迭代的完成，防止迭代器出现无限循环的情况，通常在__next()__方法中设置
class MyNumber:
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration

myclass=MyNumber()
myiter=iter(myclass)

for i in myiter:
    print(i,end=" ")