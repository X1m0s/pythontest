#接下来是一些简单的文件对象的操作方法，所有的文件操作建立在IO2.py中已创建的文件基础上

#-----1.f.read()-----
#为了读取一个文件的内容，调用f.read(size)，这将读取一定数目的数据，然后作为字符串或字节对象返回
#size是可选的数字类型的参数，当size被忽略了或者为负，那么会读取该文件的所有内容
f=open('tmp/foo.txt','r')
f_short=open('tmp/foo.txt','r')
str0=f.read();str_short=f_short.read(10)
print(str0);print(str_short)
f.close()

#-----2.f.readline()-----
#f.readline()会从文件中读取单独的一行。换行符为'\n'。f.readline()如果返回一个空字符串，说明已经读取到最后一行
f=open('tmp/foo.txt','r')
str0=f.readline();print(str0)
str0=f.readline();print(str0)
str0=f.readline();print(str0)
f.close()

#-----3.f.readlines()-----
#f.readlines()返回该文件中包含的所有行，如果设置可选参数sizehint，则读取指定长度的字节，并将字节按行分割
f=open('tmp/foo.txt','r')
str0=f.readlines()
print(str0)
f.close()
#下面是一个设置可选参数后的测试案例
f1=open("tmp/test.txt",'r')
str1=f1.readlines(10)
print(str1)
#根据文件内容可知，使用readlines()并不会把读入的行截断，而是在读n个字节后停下来并保证停在行末尾
#另一种读取方式是迭代一个文件对象然后读取每行，这种方式比readlines()耗费内存更少
#文件对象内部的迭代器__next__方法调用的是readline()函数，所以无需额外设置也会按行迭代
f=open("tmp/foo.txt","r")
for line in f:
    print(line,end='')
f.close()

#-----4.f.write()-----
#f.write(string)将string写入到文件中，然后返回写入的字符数
f=open("tmp/foo.txt","w")
num=f.write("Python是一个非常好的语言.\n是的,的确非常好!!\n")
print(num)
f.close()

#如果想要写入一些不是字符串的内容，需要先进行转换
f=open('tmp/foo1.txt','w')
value=('www.runoob.com',14)
s=str(value)
f.write(s)
f.close()
#如果想要使用不同效果的写法，可以参考下面几个例子
#1.每个元素单独一行 f.write(f"{value[0]}\n{value[1]\n}")
#2.用空格或逗号分隔 f.write(f"{value[0]},{value[1]}")
#3.把元组拆开填进模板 f.write("网站:{},编号:{}".format(*value))