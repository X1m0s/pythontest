#python中变量没有类型，类型是变量所指内存中对象的类型，使用=赋值，一个变量可通过赋值指向不同类型对象
counter=100
miles=1000.0
name="runoob"
flag=True
print(counter);print(miles);print(name);print(flag)
print(type(counter));print(type(miles));print(type(name));print(type(flag))
a=b=c=1
d,e,f=3.14,False,"runoob"
print(a,b,c,d,e,f)
print(type(a),type(b),type(c),type(d),type(e),type(f))

#python3中存在6种标准数据类型，及int子类bool类型：Number\String\bool\List\Tuple\Set\Dictionary
#不可变数据：Number(数字)、String(字符串)、bool(布尔)、Tuple(元组)
#可变数据：List(列表)、Dictionary(字典)、Set(集合)     此外存在高级数据类型，如字节数组类型bytes

#Number(数字)
#python3支持int、float、bool、complex，但仅存在一种整数类型int，表示为长整型，此外可用type()
#或isinstance()判断类型，type()不会认为子类是一种父类类型、isinstance()会认为子类是一种父类类型
#python3中，True和False可以与数字相加，True==1、False==0返回True，可以通过is判断对象身份
#但is比较的是对象身份(是否是同一对象)，而不是值是否相等。python建议使用==比较值。
#在指定值后，Number对象会被创建，可以使用del语句删除对象引用
#python3整数不允许前导0，八进制数字前缀为0o，十六进制为0x，二进制为0b

#数值运算(混合计算时，Python将整型转化为浮点型)
print(5+4)   #加法
print(4.3-2) #减法
print(3*7)   #乘法
print(2/4)   #除法，会得到浮点数
print(2//4)  #整除，只得到整数(向下取整)
print(17%3)  #取余
print(2**5)  #乘方

#python3支持复数，使用a+bj或complex(a,b)表示，复数的实部a与虚部b均为浮点型