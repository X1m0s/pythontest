#with使用中的常见问题
#1.错误认为with只能用于文件
#conn=sqlite3.connect('db.sqlite')
#仍应该使用with语句
#2.忽略__exit__的返回值
#class MyContext:
#   def __exit__(self,exc_type,exc_val,exc_tb):
#   pass
#   #忘记返回True或False可能导致异常处理不符合预期

#对于文件、网络连接、锁等资源优先使用with管理资源
with open("data.txt","r") as f:
    content=f.read()
#文件操作，自动关闭，即使中间报错也不泄露句柄
import threading
lock=threading.Lock()
with lock:
    x=1
#无论是否异常，线程锁都会自动释放，避免死锁
import sqlite3
with sqlite3.connect("database.db") as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS users(id INT)")
#数据库连接操作

#保持上下文简洁，with块中代码应该只包含与资源相关的操作
#不推荐写法(with块里塞了各种无关逻辑,后三条均与文件操作无关)
# with open("data.txt","r") as f:
#     content=f.read()
#     result=heavy_calculation(content)
#     save_to_database(result)
#     send_email(result)
#推荐写法(with只做读取,之后再处理)
with open("data.txt","r") as f:
    content=f.read()
#     result=heavy_calculation(content)
#     save_to_database(result)
#     send_email(result)

#合理处理异常，在自定义上下文管理器中，根据需求决定是否抑制异常
class SuppressError:
    def __enter__(self):
        return self
    def __exit__(self,exc_type,exc_val,exc_tb):
        if exc_type is ZeroDivisionError:
            print("除零错误已被静默忽略")
            return True                     #返回True吞掉异常，程序继续运行
        return False                        #返回False，其他异常正常往上抛    
with SuppressError():
    result=1/0                              #本来崩溃，现在错误被吞打印提示
print("程序继续运行")
#大多数情况下需要return False，让异常正常传播，只在明确知道该错误无关紧要时抑制

#利用多个上下文，Python允许在单个with语句中管理多个资源
with open("source.txt","r") as src:
    with open("dest.txt","w") as dst:
        dst.write(src.read())
#分离写法(嵌套层级多)
with open("source.txt","r") as src,open("dest.txt","w") as dst:
    dst.write(src.read())
#合并写法，用逗号分隔，从左到右依次进入，退出时从右到左
# with sqlite3.connect("db.sqlite") as conn,open("log.txt","a") as log:    
#     log.write("开始写入\n")
#     conn.execute("INSERT INTO users VALUES(1)")
#     log.write("写入完成\n")
