#with的实际应用场景示例
#-----1.文件操作-----
with open('input.txt','r') as infile,open('output.txt','w') as outfile:
    content=infile.read()
    outfile.write(content.upper())

#-----2.数据库连接-----
# import sqlite3

# with sqlite3.connect('database.db') as conn:
#     cursor=conn.cursor()
#     cursor.execute('SELECT * FROM users')
#     results=cursor.fetchall()
# #连接自动关闭

#-----3.线程锁-----
import threading

lock=threading.Lock()

with lock:
    #临界区代码
    print("这段代码是线程安全的")

#-----4.临时修改系统状态-----
import decimal 

with decimal.localcontext() as ctx:
    ctx.prec=42     #临时设置为高精度
    #执行高精度计算
#精度恢复原设置

#创建自定义的上下文管理器
#1.类实现方式，可以在一个类中实现__enter__和__exit__方法来创建自定义的上下文管理器
class Timer:
    def __enter__(self):
        import time
        self.start=time.time()
        return self
    def __exit__(self,exc_type,exc_val,exc_tb):
        import time
        self.end=time.time()
        print(f"耗时:{self.end-self.start:.2f}秒")
        return False
#返回False的含义为如果上下文内部发生异常，不要吞掉继续向上抛出，如果返回True内部报错会被静默掩盖
with Timer() as t:          
    sum(range(1000000))

print(t.start,t.end)

#2.使用contextlib模块，该模块提供了更简单的方式来创建上下文管理器
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")
with tag("h1"):
    print("这是一个标题")
