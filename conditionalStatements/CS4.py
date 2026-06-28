#match语句是python3.10引入的结构化模式匹配语句，类似于switch-case，但功能更强大
#match可用于匹配数据结构的模式，不仅可以是常量值，也可以是类型、序列、字典等复杂模式
#语法格式为:match 变量:
#               case 模式1:
#                   代码块1
#               case 模式2:
#                   代码块2
#               case _:
#                   默认代码块
#模式类型:常量模式-匹配具体值，通配符模式-case _匹配任何值，相当于default，类型模式-匹配数据类型
#序列模式-匹配列表、元组等序列，字典模式-匹配字典，带条件的模式-使用if添加额外条件
#特殊模式-捕获模式
#基础用法1
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown"
print(http_status(200),http_status(404),http_status(999))
#case _类似于switch-case中的default
#基础用法2-多值匹配
def color_name(code):
    match code:
        case "r"|"R":
            return "红色"
        case "g"|"G":
            return "绿色"
        case "b"|"B":
            return "蓝色"
        case _:
            return "未知颜色"
print(color_name("r"))
print(color_name("G"))
print(color_name("x"))
#基础用法3-序列模式匹配
def describe_point(point):
    match point:
        case (0,0):
            return "原点"
        case (x,0):                      #捕获模式，第一个元素任意，但必须为二元素且第二元素为0
            return f"x轴上的点({x},0)"
        case (0,y):
            return f"y轴上的点(0,{y})"
        case (x,y):
            return f"平面上的点({x},{y})"
        case _:
            return "无效坐标"
print(describe_point((0,0)),describe_point((5,0)),describe_point((3,4))) #match可以解构元组/列表提取值
#基础用法4-字典模式匹配
def process_user(user):
    match user:
        case {"name":name,"age":age}:
            return f"用户:{name},年龄:{age}"
        case {"name":name}:
            return f"用户:{name}"
        case _:
            return "无效用户"

print(process_user({"name":"Tom","age":20}))
print(process_user({"name":"Jerry"}))
print(process_user({"role":"admin"}))
#字典模式可以提取特定键的值
#基础用法5-带条件的模式
def classify_number(n):
    match n:
        case n if n>0:
            return f"正数({n})"
        case n if n<0:
            return f"负数({n})"
        case 0:
            return "零"
print(classify_number(10))
print(classify_number(-5))
print(classify_number(0))
#复杂条件
def describe_list(lst):
    match lst:
        case []:
            return "空列表"
        case [x]:
            return f"单个元素:{x}"
        case [x,y]:
            return f"两个元素:{x},{y}"
        case [x,*rest]:
            return f"第一个:{x},其余:{rest}"
print(describe_list([]))
print(describe_list([1]))
print(describe_list([1,2,3,4]))