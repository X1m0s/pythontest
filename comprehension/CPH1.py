#python推导式是一种独特的数据处理方式，可从一个数据序列构建另一个新数据序列的结构体
#适用于生成列表、字典和生成器，分为列表推导式、字典推导式、集合推导式、元组推导式

#列表推导式的格式为:
#[表达式 for 变量 in 列表]————[out_exp_res for out_exp in input_list]
#或者:
#[表达式 for 变量 in 列表 if 条件]————[out_exp_res for out_exp in input_list if condition]
#out_exp_res为列表生成元素表达式，可以是有返回值的函数，也可以只是用于接受迭代数据的变量本身
#for out_exp in input_list:迭代input_list将out_exp传入到out_exp_res表达式中
#if condition用于过滤列表中不符合条件的值
#示例如下
#if过滤长度小于3的字符串，.upper()将元素转成大写字母
names=["Bob","Tom","alice","Jerry","Wendy","Smith"]
new_names=[name.upper() for name in names if len(name)>3]   
print(new_names)
#计算30以内可被3整除的整数
nums=[num for num in range(31) if num%3==0]
print(nums)

#字典推导式的格式为:
#{key_expr:value_expr for key/value in collection}
#或者:
#{key_expr:value_expt for key/value in collection if condition}
#示例如下
#使用列表中各字符串值为键，长度为值，组成键值对
listdemo=["Google","Runoob","Taobao"]
newdict={key:len(key) for key in listdemo}
print(newdict)
#提供三个数字，以数字为键，三个数字的平方为值来创建字典
dic={x:x**2 for x in [2,4,6]}
print(dic,type(dic))

#集合推导式的格式为:
#{expression for item in Sequence}
#或者:
#{expression for item in Sequence if conditional}
#示例如下:
setnew={i**2 for i in [1,2,3]}
print(setnew,type(setnew))
#判断不是abc的字母并输出
a={x for x in "abracadabra" if x not in "abc"}
print(a,type(a))

#元组推导式(生成器表达式)的格式为:
#(expression for item in Sequence)
#或者:
#(expression for item in Sequence if conditional)
#需要注意的是，其他推导式返回的都是对应的数据类型，因为()被生成器表达式占用元组推导式返回的是生成器对象
#示例如下
a=(x for x in range(1,10))
print(a,type(a))
print(tuple(a))             #生成器对象可被重新转换为元组

#推导式中 if 的两种位置
#位置1: for 前面 — 条件表达式（三元运算符），每个元素必经此判断
# [值A if 条件 else 值B for 变量 in 可迭代对象]
#           必须有 else ──┘

#位置2: for 后面 — 过滤条件，不满足的直接丢弃，没有 else
# [表达式 for 变量 in 可迭代对象 if 条件]
#                               ↑ 不满足则跳过该元素

#示例1: for 前的 if-else — 每个元素都返回值（两种可能）
list1 = ['python', 'test1', 'test2']
list2 = [word.title() if word.startswith('p') else word.upper() for word in list1]
print(list2)  # ['Python', 'TEST1', 'TEST2']
# p 开头 → title 首字母大写, 否则 → 全大写

#示例2: for 后的 if — 不满足的元素直接丢弃
nums = [x for x in range(10) if x % 2 == 0]
print(nums)  # [0, 2, 4, 6, 8]
# 只保留偶数，奇数跳过

#示例3: 两者同时使用 — 先过滤再判断
result = [x*2 if x > 2 else x for x in range(6) if x != 0]
#                                             ↑ 过滤:跳过0
#                   ↑ 条件表达式:>2翻倍,≤2原样
print(result)  # [1, 2, 6, 8, 10]
# 0跳过 → 1原样 → 2原样 → 3翻倍 → 4翻倍 → 5翻倍