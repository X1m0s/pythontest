#-----4.seed()-----
#seed()函数可以改变随机数生成器的种子，在调用其他随机模块函数前调用此函数
#参数支持所有可哈希值，当不传递参数或为None时，自动调用系统时间作为种子
#seed(x,version)，x为种子值，version为哈希算法版本(取值仅有1和2)，默认使用新版哈希即2
#此外random.seed()设置的种子仅对同模块生成器生效
import random
random.seed(12)
print(random.random())
print(random.randrange(100))
random.seed(42)
print(random.random())
print(random.randrange(100))
random.seed(12)
print(random.random())
print(random.randrange(100))
random.seed("hello",2)
print(random.random())
print(random.randrange(100))
#-----5.shuffle()-----
#shuffle(lst)函数用于随机排序序列中所有元素，lst为可变序列，不支持元组、字符串、集合
test_list=[10,20,30,40,50]
random.shuffle(test_list)
print("随机排序后的列表为:",test_list)      #shuffle会修改原序列，如果保留原序列需要提前拷贝
#-----6.uniform-----
#uniform(x,y)用于生成一个在[x,y]范围内的浮点型实数
print("uniform(5,10)的随机浮点数=",random.uniform(5,10))
print("uniform(7,14)的随机浮点数=",random.uniform(7,14))
print("uniform(12,4)的随机浮点数=",random.uniform(12,4))    #当x>y时，函数会自动调整上下界