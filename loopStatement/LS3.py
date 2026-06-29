#break是python中用于立即终止循环的关键字
#当程序执行到break时，会立即跳出当前的循环结构(无论是for或while)，不再执行剩余代码
#常用于提前退出循环/找到目标后退出搜索/配合无限循环作为退出
#基础用法1-在for中使用
numbers=[1,3,5,6,7,8,9]
for num in numbers:
    if num%2==0:
        print(f"找到了第一个偶数,是{num}")
        break
print("搜索结束")
#基础用法2-在while循环中使用
total=0;i=1
while True:
    total+=i
    if total>100:
        print(f"当i={i}时,总和首次超过100")
        break
    i+=1
print(f"总和:{total}")
#基础用法3-嵌套循环中的break
for i in range(1,4):
    for j in range(1,4):
        if i==2 and j==2:
            break                           #仅退出当前层循环
        print(f"{i},{j}",end=" ")
    print()
#基础用法4-配合else使用
for i in range(5):
    if i==3:
        print("找到目标,提前退出")
        break
    print(i)
else:
    print("循环正常结束,未找到目标")
print("---")
for i in range(5):
    print(i)
else:
    print("循环正常结束,else执行")