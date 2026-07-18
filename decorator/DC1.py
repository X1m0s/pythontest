#装饰器是python中的高级功能，用于在不修改原函数代码的前提下，动态扩展函数或类的功能
#本质上，装饰器是一个函数，接收函数作为参数，并返回一个新函数(通常为原函数的增强版本)
#装饰器通过@decorator_name语法应用在函数或方法定义之前
#python也提供了一些内置装饰器，如@staticmethod和@classmethod
#通常用于日志记录(记录函数调用信息、参数和返回值)、性能统计(统计函数执行时间)、
#权限控制(限制函数访问权限)、缓存(缓存函数结果，提高性能)等场景中

#基本语法(装饰器的核心思想是用一个函数"包装"另一个函数)
def decorator_function(original_function):
    def wrapper(*args,**kwargs):
        #调用前
        print("执行前")
        result=original_function(*args,**kwargs)
        #调用后
        print("执行后")
        return result
    return wrapper

@decorator_function
def target_funcion():
    print("原函数执行")
#decorator_function:装饰器函数(用于接收原函数)  等价于函数替换
#wrapper:包装函数(真正执行的函数)
#等价于target_function=decorator_function(target_function) #实际执行的是wrapper()

#下面是一个使用装饰器的实例
def my_decorator(func):
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
say_hello()

#下面是一个使用有参装饰器的实例(在原函数有参情况下，需要在wrapper中使用*args,**kwargs)
#但在装饰器中，使用*args和**kwargs都是用作参数转发，前者控制位置参数，后者控制关键字参数
#定义时使用*args是用于把多个位置参数打包进一个元组，本质为收集
#调用时使用*args则是用于把一个元组拆散成多个位置参数，本质为分发
def my_decorator1(func):
    def wrapper(*args,**kwargs):
        print("执行前")
        func(*args,**kwargs)
        print("执行后")
    return wrapper

@my_decorator1
def greet(name):
    print(f"Hello,{name}")
greet("Alice")

#一个装饰器工厂实例
def repeat(num_times):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                func(*args,**kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello1():
    print("Hello!")
say_hello1()
#在这个装饰器工厂中，repeat层用于接收参数num_times，decorator层用于接收被装饰的函数，wrapper用于替换原函数执行
#三层函数都不可缺少，第一层没了无法传入3，第二层没了@不知道装饰哪个函数，第三层没了原函数被完全丢弃
