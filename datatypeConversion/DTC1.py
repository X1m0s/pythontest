#python的数据类型转换分为两种:隐式转换(自动完成)、显式转换(需要使用类型函数)
#当对不同类型数据进行运算时，精度较低的数据类型会转换为精度较高的数据类型，以避免数据丢失
num_int=123;num_flo=1.23
num_new=num_int+num_flo
print("num_int数据类型为：",type(num_int))
print("num_flo数据类型为：",type(num_flo))
print("num_new值为:",num_new,"num_new数据类型为：",type(num_new))

num_int=123;num_str="456"
print("num_int数据类型为：",type(num_int))
print("num_str数据类型为：",type(num_str))
#print(num_int+num_str)
#当整型与字符串型运算时会报错TypeError: unsupported operand type(s) for +: 'int' and 'str'
#这种情况下python不进行隐式转换

