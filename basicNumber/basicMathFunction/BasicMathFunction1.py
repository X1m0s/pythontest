#-----1.abs()-----
print("abs(-40)=",abs(-40))         #abs()函数通常用于计算绝对值
print("abs(100.10)=",abs(100.10))
print("abs(3+4j)=",abs(3+4j))       #当abs()内参数为复数时，改为计算复数的模，即计算√(a²+b²)
#-----2.ceil()-----
import math                                         #本处介绍的math模块函数均不支持复数
print("math.ceil(-45.17)=",math.ceil(-45.17))       #且所有math函数返回值均为浮点型
print("math.ceil(100.12)=",math.ceil(100.12))       #ceil()函数不能直接访问，需要导入math模块
print("math.ceil(100.72)=",math.ceil(100.72))       #该函数用于向上取整，返回一个>=x的最小整数
print("math.ceil(math.pi)=",math.ceil(math.pi))
#-----3.cmp()-----
#如果x<y返回-1,如果x==y返回0,如果x>y返回1，python3中已废弃，使用(x>y)-(x<y)获得相同效果，不做演示
#-----4.exp()-----
print("math.exp(0)=",math.exp(0))           #该函数用于计算e的x次幂
print("math.exp(1)=",math.exp(1))
print("math.exp(2)=",math.exp(2))
print("math.exp(2)==math.e ** 2=",math.exp(2)==math.e ** 2)     
print("math.exp(2)≈math.e ** 2=",math.isclose(math.exp(2),math.e ** 2)) #isclose()函数用于比较浮点数
#效果相同但exp()函数精度略高
#变体:
print("math.exp2(16)=",math.exp2(16))
#-----5.fabs()-----
#fabs()函数永远以浮点数形式返回参数的绝对值，与abs()函数不同，abs在参数为整数时返回整数
#函数功能类似于abs()函数，但fabs()函数不是内置函数
print("x=",x:=-1.5," x的绝对值y=",y:=math.fabs(x),sep="")
print("x=",x:=10," x的绝对值y=",y:=math.fabs(x),sep="")
#-----6.floor()-----
print("math.floor(-45.17)=",math.floor(-45.17))     #floor()函数用于向下取整，返回一个<=x的整数
print("math.floor(100.12)=",math.floor(100.12))
print("math.floor(100.72)=",math.floor(100.72))
print("math.floor(math.pi)=",math.floor(math.pi))
#-----7.log()-----
print("math.log(100,10)=",math.log(100,10))         #log(x,base)用于求base的几次方等于x
print("math.log(8,2)=",math.log(8,2))   
print("math.log(math.e)=",math.log(math.e))         #log(x)的默认base值为e，这时与exp互逆
print("math.log(1)=",math.log(1))
#变体:
print("math.log2(8)=",math.log2(8))                 #以下为log()函数的变体
print("math.log10(100)=",math.log10(100))
#log1p(x)等价于ln(1+x)，在x接近0时，对极小值精确度更高
#伴生函数expm1等价于e**x-1，在x极小时更精确
print("math.log(1+1e-15)=",math.log(1+1e-15))
print("math.log1p(1e-15)=",math.log1p(1e-15))
print("math.log1p(1e-15)==math.log(1+1e-15)",math.log1p(1e-15)==math.log(1+1e-15))  #当x很小时≠
