#除了函数，装饰器也可作用于类，类装饰器接受一个类，并返回修改后的类或包装类
#通常用于增强类方法、控制实例化过程以及实现单例、日志等功能
#下面是一个函数形式的类装饰器实例
from typing import Any


def log_class(cls):
    class Wrapper:
        def __init__(self,*args,**kwargs):
            self.wrapped=cls(*args,**kwargs)
        def __getattr__(self,name):
            return getattr(self.wrapped,name)
        def display(self):
            print("调用前")
            self.wrapped.display()
            print("调用后")
    return Wrapper

@log_class
class MyClass:
    def display(self):
        print("原方法")

obj=MyClass()
obj.display()
#该模式下装饰器将原始类替换成wrapper类，每次会新建wrapper实例，但原始类的方法会被Wrapper的方法拦截/增强
#通常用于日志、权限检查、方法增强

#下面是一个类形式的类装饰器，单例模式
class SingletonDecorator:
    def __init__(self,cls):
        self.cls=cls
        self.instance=None

    def __call__(self,*args,**kwargs):
        if self.instance is None:
            self.instance=self.cls(*args,**kwargs)
        return self.instance
    
@SingletonDecorator
class Database:
    def __init__(self):
        print("初始化")

db1=Database()
db2=Database()
print(db1 is db2)
#该模式下装饰器一直使用同一个原始实例进行替换，而非创建新对象，原始类的方法也完全保留
#通常用于单例模式、连接池复用

#多个装饰器堆叠(即在定义阶段从下到上依次包裹函数时)，调用阶段从上到下依次执行
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper
def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()

#总结：装饰器=函数包装函数+不修改原代码扩展功能     @语法本质是函数替换     wrapper是真正执行函数
#推荐使用*args,**kwargs提高通用性    支持函数、类、甚至带参数的装饰器