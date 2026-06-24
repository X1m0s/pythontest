#本节提及的所有三角函数均来源于math模块
#-----1.sin()&cos()&tan()-----
#参数必须为实数，导入后会自行转换为弧度制
import math
print("math.sin(0)=",math.sin(0),"math.cos(0)=",math.cos(0),"math.tan(0)=",math.tan(0))
print("math.sin(math.pi/2)=",math.sin(math.pi/2),"math.cos(math.pi/2)=",math.cos(math.pi/2),
      "math.tan(math.pi/2)=",math.tan(math.pi/2))
print("math.sin(30)=",math.sin(30),"math.cos(30)=",math.cos(30),"math.tan(30)=",math.tan(30))
#如果需要导入角度，需要使用math.radians()函数
#-----2.asin()&acos()&atan()-----
#参数必须为一个在-1到1之间的数值
print("math.asin(0)=",math.asin(0),"math.acos(0)=",math.acos(0),"math.atan(0)=",math.atan(0))
print("math.asin(0.5)=",math.asin(0.5),"math.acos(0.5)=",math.acos(0.5),
      "math.atan(0.5)=",math.atan(0.5))
print("math.asin(1)=",math.asin(1),"math.acos(1)=",math.acos(1),"math.atan(1)=",math.atan(1))
#-----3.atan2()-----
#用于计算给定坐标(x,y)的反正切值
print("atan2(-0.5,-0.5)=",math.atan2(-0.5,-0.5))  #atan2(y,x)函数的参数顺序与常见顺序相反，先y后x
print("atan2(0.5,0.5)=",math.atan2(0.5,0.5))     
print("atan2(5,-5)=",math.atan2(5,-5))
print("atan2(-10,20)=",math.atan2(-10,20))
#-----4.hypot()-----
#用于计算欧几里得范数sqrt(x**2+y**2)————其实就是算勾股定理
print("hypot(3,4)=",math.hypot(3,4))
print("hypot(5,12)=",math.hypot(5,12))
print("hypot(1,0.5)=",math.hypot(1,0.5))
#-----5.degrees()&radians()-----
#两个函数分别用于把给定的数值转换为角度值和弧度值，角度与弧度的关系为2Π弧度=360°
#弧度=角度/180*Π  角度等于弧度*180/Π
print("degrees(3):",math.degrees(3))
print("degrees(-3):",math.degrees(-3))
print("degrees(0):",math.degrees(0))
print("degrees(math.pi):",math.degrees(math.pi))
print("degrees(math.pi/2):",math.degrees(math.pi/2))
print("degrees(math.pi/4):",math.degrees(math.pi/4))

print("radians(90)=",math.radians(90))     # 1 弧度等于大概 57.3°
print("radians(45)=",math.radians(45))
print("radians(30)=",math.radians(30))
print("radians(180)=",math.radians(180))  # 180 度的弧度为 π
print("180/pi",end ="") 
print(math.radians(180/math.pi))