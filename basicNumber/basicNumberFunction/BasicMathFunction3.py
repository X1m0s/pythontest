#本节所有函数均为math模块函数，仅作为拓展
#-----13.trunc()-----
import math
print("math.trunc(3.14)=",math.trunc(3.14))         #trunc()函数用于截断小数部分，不进行舍入操作
print("math.trunc(-3.14)=",math.trunc(-3.14))
print("math.trunc(3.69)=",math.trunc(3.69)) 
print("math.ceil(3.14)=",math.ceil(3.14))           #ceil向上
print("math.floor(3.14)=",math.floor(3.14))         #floor向下
#-----14.factorial()-----
print("math.factorial(5)=",math.factorial(5),"type(math.factorial(5))=",type(math.factorial(5)))
print("math.factorial(0)=",math.factorial(0))       #factorial()用于计算阶乘,仅接受整型参数 
#-----15.gcd()&lcm()-----
#gcd()和lcm()分别用于计算两个整数的最大公约数和最小公倍数，要求必须为整型参数且返回值为整型
print("math.gcd(12,8)=",math.gcd(12,8),"math.gcd(17,5)=",math.gcd(17,5))    #返回1时说明互质
#gcd=Greatest Common Divisor
print("math.lcm(12,8)=",math.lcm(12,8),"math.lcm(3,5)=",math.lcm(3,5))
#lcm=Least Common Multipie
#python3.9中实装了lcm()函数以及两个函数的多参数扩展
print("math.gcd(12,8,4,2)=",math.gcd(12,8,4,2))
print("math.lcm(12,15,4)=",math.lcm(12,15,4))
#-----16.comb()-----
#用于计算组合数，即C(n,k)=n!/(k!*(n-k)!)，comb(a,b)中a=n、b=k
print("math.comb(5,2)=",math.comb(5,2))
print("math.comb(5,3)=",math.comb(5,3))
