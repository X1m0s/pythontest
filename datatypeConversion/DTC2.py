#显式类型转换

#int()强制转换为整型:
x=int(1);y=int(2.8);z=int("3")
print(x,y,z)

#float()强制转换为浮点型:
x=float(1);y=float(2.8);z=float("3");w=float("4.2")
print(x,y,z,w)

#str()强制转换为字符串类型:
x=str("s1");y=str(2);z=str(3.0)
print(x,y,z)

#整型和字符串类型进行运算
num_int=123;num_str="456"
print("num_int数据类型为：",type(num_int))
print("类型转换前，num_str数据类型为：",type(num_str))
num_str=int(num_str)
print("类型转换后，num_str数据类型为：",type(num_str))
num_sum = num_int + num_str
print("num_int与num_str相加结果为:",num_sum)
print("sum数据类型为:",type(num_sum))