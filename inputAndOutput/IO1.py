#输出格式美化
#python输出值的方式有表达式语句和print()函数
#第三种方式是使用文件对象的write()方法，标准输出文件可以用sys.stdout引用
#如果希望输出的形式更加多样，可以使用str.format()函数来格式化输出值
#如果希望输出的值转为字符串，可以使用repr()或str()来实现 
#str()函数返回一个用户易读的表达形式    repr()产生一个解释器易读的表达形式

s='Hello,Runoob'
print(str(s))
print(repr(s))
print(str(1/7))
x=10*3.25;y=200*200
s='x的值为:'+repr(x)+',y的值为:'+repr(y)+'...'
print(s)
#repr()函数可以转义字符串中的特殊字符
hello='hello,runoob\n'
hellos=repr(hello)
print(hellos)
#repr()的参数可以是Python的任何对象
print(repr((x,y,('Google','Runoob'))))

#下面是用两种方式来输出一个平方与立方的表
for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
    print(repr(x*x*x).rjust(4))

for x in range(1,11):
    print('{0:2d}{1:3d}{2:4d}'.format(x,x*x,x*x*x))

#str.format()的基本使用如下
print('{}网址: {}!'.format('菜鸟教程','www.runoob.com'))
#括号及其里面的字符(称作格式化字段)将会被format()中的参数替换，在括号中的数字用于指向传入对象在format()中的位置
print('{0}和{1}'.format('Google','Runoob'))
print('{1}和{0}'.format('Google','Runoob'))
#如果在format()中使用了关键字参数，那么它们的值会指向使用该名字的参数
print('{name}网址:{site}'.format(name='菜鸟教程',site='www.runoob.com'))
#位置和关键字参数可以任意的结合
print('站点列表{0},{1}和{other}。'.format('Google','Runoob',other='Taobao'))
#!a(使用ascii())，!s(使用str())和!r(使用repr())可以用于在格式化某个值之前对其进行转化:
import math
print('常量PI的值近似为:{}。'.format(math.pi))
print('常量PI的值近似为:{!r}。'.format(math.pi))
#可选项:和格式标识符可以跟着字段名，这就允许对值进行更好的格式化
print('常量PI的值近似为:{0:.3f}。'.format(math.pi))
#在:后传入一个整数，可以保证该域至少有这么多的宽度，用于美化表格时很有用
table={'Google':1,'Runoob':2,'Taobao':3}
for name,number in table.items():
    print('{0:10} ==> {1:10d}'.format(name,number))
#如果有一个很长的格式化字符串，而你不像把它们分开，在格式化时通过变量名而非位置更为高效，最简单的方式就是传入一个字典，使用[]访问键值
table={'Google':1,'Runoob':2,'Taobao':3}
print('Runoob:{0[Runoob]:d};Google:{0[Google]:d};Taobao:{0[Taobao]:d}'.format(table))
#如果不想使用0来让format指定取第0个table，也可以在table前加**来拆开字典，效果是一样的
print('Runoob:{Runoob:d};Google:{Google:d};Taobao:{Taobao:d}'.format(**table))
