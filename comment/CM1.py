"""
三个引号包围的文本块为多行字符串，该字符串只要不被使用，就不会影响程序运行
因此可以用作多行注释，但是多行注释不能进行嵌套
当开始一个多行注释块时，python会一致将后续的行都当作注释，直到遇到另一组引号
#所以正确做法是在多行注释中使用单行注释进行嵌套
"""
#Docstring文档字符串是python中一种特殊注释，用于为类、函数、模块添加文档说明，类似于Javadoc
#与普通注释不同，Docstring可通过__doc__属性访问，也可以用help()函数查看
#Docstring使用三个引号包围，放在函数、模块、类的开头
def add(a,b):
    """返回两数之和"""
    return a+b
#通过__doc__属性访问
print(add.__doc__)
#inspect模块也可以提取文档内容
#inspect.getdoc(obj)提取对象的文档字符串，并自动清理公共缩进空白
#inspect.getsource(obj)可直接提取对象源码
import inspect
print(inspect.getdoc(add))    #使用inspect.getdoc()获取文档
print(inspect.getsource(add)) #提取该函数源码

#对于复杂函数，可以使用多行Docstring
def calculate(a,b,operation="add"):
    """
    进行数学运算

    参数:
        a:第一个数字
        b:第二个数字
        operation:操作类型，可选"add","subtract","multiply"

    返回:
        计算结果
    """
    if operation=="add":
        return a+b
    elif operation=="subtract":
        return a-b
    elif operation=="multiply":
        return a*b
    else:
        raise ValueError("不支持的操作")
print(inspect.getdoc(calculate))

#Docstring同样可应用于类
class Person:
    """人物类，用于表示一个人的基本信息"""

    def __init__(self,name,age):
        """
        初始化人物对象

        参数：
            name:姓名
            age:年龄
        """
        self.name=name
        self.age=age
    def introduce(self):
        """介绍这个人"""
        return f"我叫{self.name},今年{self.age}岁"

#访问类的文档
print(Person.__doc__)
#访问方法的文档
print(Person.__init__.__doc__)
print(Person.introduce.__doc__)