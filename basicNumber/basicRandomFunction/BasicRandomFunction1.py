#-----1.choice()-----
#choice()函数属于random模块内部函数，需导入后使用
import random
test_list=[1,3,5,7,9,0,2,4,6,8]
test_str="HelloWorld"
test_tup=(1,3,5,7,9,0,2,4,6,8)
print("1st-random.choice(test_list)=",random.choice(test_list))
print("1st-random.choice(test_str)=",random.choice(test_str))
print("1st-random.choice(test_tup)=",random.choice(test_tup))
print("1st-random.choice([1,3,5,7,9])=",random.choice([1,3,5,7,9]))
#每次执行命令生成随机数时种子不同
print("2nd-random.choice(test_list)=",random.choice(test_list))
print("2nd-random.choice(test_str)=",random.choice(test_str))
print("2nd-random.choice(test_tup)=",random.choice(test_tup))
print("2nd-random.choice([1,3,5,7,9])=",random.choice([1,3,5,7,9]))
#变体:
#choices()函数为3.6版本对choice()函数的功能扩展，参数为choices(seq,weights/cum_weights,k)
#其中seq为随机抽取样本的序列，weights为权重，cum_weights为累积权重，与权重二选一使用，k为随机输出次数
print("1st-random.choices([1,2,3,4],weights=[1,5,1,1],k=5)=",
      random.choices([1,2,3,4],weights=[1,5,1,1],k=5))
print("2nd-random.choices([1,2,3,4],weights=[1,5,1,1],k=5)=",
      random.choices([1,2,3,4],weights=[1,5,1,1],k=5))
print("3rd-random.choices([1,2,3,4],weights=[1,5,1,1],k=5)=",
      random.choices([1,2,3,4],weights=[1,5,1,1],k=5))

#下面是一个随机密码生成器示例
import random
import string

def password_generator(length):
    #定义密码可用字符集合，其中ascii_letters包含所有大小写字母，digits包含所有数字
    #punctuation包含所有标点符号
    chars=string.ascii_letters+string.digits+string.punctuation     #char为拼接字符串
    password=''.join((random.choice(chars)) for _ in range(length)) #此处for为生成器表达式
    return password
random_pwd=password_generator(6)
print(random_pwd)
#-----2.randrange()-----
#randrange()函数属于random模块内部函数，用于返回指定递增基数集合中的一个随机数，基数默认值是1
#randrange(start,stop,step)的参数含义分别为开始值(包含)，结束值(不包含)，步长(递增基数)
#只有结束值为必要参数，其余参数为可选
print("randrange(100)=",random.randrange(100))        #从0-99选取一随机数
print("randrange(50,100)=",random.randrange(50,100))  #从50-99选取一随机数
print("randrange(1,100,2)=",random.randrange(1,100,2))#从1-99选取一个奇数
#-----3.random()-----
#用于生成一个0-1之间的随机浮点数，范围为[0,1)
print("第一个浮点数:",random.random())
print("第二个浮点数:",random.random())
print("第三个浮点数:",random.random())
