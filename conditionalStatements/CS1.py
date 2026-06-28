#条件控制语句是通过一条或多条语句的执行结果来决定执行的代码块
#if语句是最基本的条件控制结构，根据条件真假决定是否执行特定代码块
#语法格式为if 条件表达式:       #条件表达式为任何返回布尔值的表达式(非0，非空字符串，非空容器视为真)
#             代码块            #条件表达式后必须加冒号，代码块必须进行缩进，通常4空格
#if语句本身为控制流语句，不返回任何值，当条件为True时执行缩进的代码块，否则跳过
#基础用法1-判断数字大小
age=18
if age>=18:
    print("chengnian")
#基础用法2-判断字符串是否为空
name=""                         #字符串为空时为False
if name:                        #所有空字符、列表、字典等在条件判断是均视为False
    print(f"你好,{name}")
else:
    print("请输入名字")
name="Tom"
if name:
    print(f"你好,{name}")
else:
    print("请输入名字")
#基础用法3-多条件判断
score=85
if score>=60 and score<90:
    print("及格了")
if 60<=score<90:                #python特有的链式比较
    print("成绩在60-90之间")
colors=["red","green","blue"]
if "red" in colors:
    print("包含红色")
#基础用法4-单行if表达式(三元运算符)
age=20
#python的三元表达式比传统语言更简洁，格式:value1 if 条件 else value2
result="成年" if age>=18 else "未成年"
print(result)
#另外一个示例
x=10;y=20
max_val=x if x>y else y
print(f"较大值:{max_val}")
#elif适用于多条件判断，为else if的缩写，允许串列多个条件判断，以形成分支结构
#必须与if配合使用，不能单独存在
#基础用法1-基础多条件判断
score=85
if score>=90:
    grade="A"
elif score>=80:
    grade="B"
elif score>=70:
    grade="C"
elif score>=60:
    grade="D"
else:
    grade="F"
print(f"成绩等级:{grade}")
#基础用法2-字符串匹配
choice="2"
if choice=="1":
    print("你选择了新建文件")
elif choice=="2":
    print("你选择了打开文件")
elif choice=="3":
    print("你选择了保存文件")
elif choice=="4":
    print("你选择了退出")
else:
    print("无效选择")
#基础用法3-复杂的条件组合
age=25
income=5000
if age<18:
    print("未成年人")
elif age>=18 and income<3000:
    print("成年人,低收入")
elif age>=18 and income>=3000 and income<10000:
    print("成年人,中等收入")
elif age>=18 and income>=10000:
    print("成年人,高收入")
#使用elif实现更清晰逻辑
status="error"
if status=="success":
    print("操作成功")
elif status=="error":
    print("操作失败")
elif status=="warning":
    print("警告")
elif status=="info":
    print("信息")