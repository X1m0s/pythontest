#else语句用于处理其他所有情况，当所有条件都不满足时再执行，必须配合if使用，作为条件判断结构结尾
#基础用法1
age=15
if age>=18:
    print("成年人")
else: 
    print("未成年人")
#奇偶数判断
num=7
if num%2==0:
    print(f"{num}是偶数")
else:
    print(f"{num}是奇数")
#基础用法2-与elif配合
score=55
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
print(f"分数:{score},等级:{grade}")
#基础用法3-处理异常情况
#登录验证示例
username="admin"
password="wrong"
if username=="admin" and password=="123456":
    print("登陆成功")
else:
    print("登陆失败，检查用户名或密码")
#处理空列表情况
items=[]
if items:
    print(f"列表有{len(items)}个元素")
else:
    print("列表为空")
#文件操作中的else
try:                                #else可用于try-except结构，表示没有异常时的处理
    result=10/2
except ZeroDivisionError:
    print("不能除以零")
else:
    print(f"计算结果:{result}") 