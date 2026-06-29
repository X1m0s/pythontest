#continue用于跳过当次循环，进入下一次迭代
#通常用于满足条件时跳过处理、排除不符合条件的数据、将"不处理"的条件提前,减少嵌套
#基础用法1
for i in range(1,11):
    if(i%2==0):
        continue
    print(i,end=" ")
print()
#基础用法2-过滤列表元素
data=["apple",None,"","banana"," ","cherry"]
result=[]
for item in data:
    if not item:
        continue
    result.append(item)
print(result)
#另一种思路,仅处理有效元素
print("有效数据:")
for item in data:
    if item:
        print(f"-{item}")
#基础用法3-在while循环中使用
n=0
while n<10:
    n+=1
    if n==5 or n==7:
        continue
    print(n,end=" ")
print()
#基础用法4-简化代码逻辑
numbers={1,2,-3,4,-5,6,-7}
#不使用continue时
print("正数(方式1):")
for n in numbers:
    if n>0:
        print(n)
print("\n正数(方式2)-使用continue:")
for n in numbers:
    if n<=0:
        continue
    print(n)
print("\n负数:")
for n in numbers:
    if n>=0:
        continue
    print(n)
#基础用法5-嵌套循环中的continue
for i in range(1,4):
    for j in range(1,4):
        if j==2:
            continue            #此时仅跳过内层本次迭代
        print(f"({i},{j})",end=" ")
    print()