#pass语句是python中的空语句，也成为占位语句
#pass语句不进行任何操作，只作为一个占位符，保证代码语法完整性，常用于暂时不想写具体实现的代码块中
#使用场景为：空代码块、函数占位、类占位、条件占位
#基础用法1-if语句中使用
age=20
if age>=18:
    pass            #TODO:需要添加年龄验证逻辑
else:
    print("未成年")
print("程序继续运行")
#如果不加pass，代码块为空时会报错
#基础用法2-函数中使用
#定义一个空函数
def placeholder_function():
    pass

#调用函数 
placeholder_function()
print("函数已调用")

#带条件的空函数
def process_data(data):
    if not data:
        pass                #数据为空，暂不处理
        return
    return data.upper()     #实际的处理逻辑
print(process_data("hello"))
print(process_data(""))
#定义函数时，如果函数体暂时为空，必须使用pass占位
#基础用法3-类中使用
#定义一个空类
class EmptyClass:
    pass
#实例化
obj=EmptyClass()
print(obj)
#类中定义空方法
class TodoClass:
    def method1(self):
        pass
    def method2(self):
        return"已完成"
obj=TodoClass()
print(obj.method2())
#空类或空方法可以使用pass占位，后续实现具体功能
#基础用法4-循环中使用
#遍历但是什么都不做
for i in range(5):
    pass                #暂时不处理
print("循环完成")
#配合条件使用
for i in range(10):
    if i%2==0:
        pass            #偶数不处理
    else:
        print(i,end=" ")
#输出:1 3 5 7 9