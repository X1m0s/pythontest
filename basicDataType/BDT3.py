#列表用方括号[]包围，用逗号,分隔开
#列表中元素类型可以不同，支持数字、字符串以及嵌套列表
#和字符串一样，列表可以被索引和截取，列表在被截取后返回一个包含所需元素的新列表
#列表截取格式->变量名[头下标:尾下标]，包含头下标，不包含尾下标，索引时以0为开始值，-1为末尾起始位
#列表示例：
#         t=["a","b","c","d","e"]
#从前索引:    0   1   2   3   4
#从后索引    -5  -4  -3  -2  -1
# t[1:3]->["b","c"]  t[3:]->["d","e"]
# t[:4]->["a","b","c","d"]  t[:]->["a","b","c","d","e"]

my_list=["abcd",486,2.23,"runoob",70.2]
tinylist=[123,"runoob"]
print(my_list)          #打印整个列表
print(my_list[0])       #打印第一个元素
print(my_list[1:3])     #打印第二个、第三个元素、不包含第四个
print(my_list[2:])      #从第三个元素开始打印，包括第三个元素
print(tinylist*2)       #重复打印列表两次
print(my_list+tinylist) #拼接两个列表

#与字符串不同，列表内元素是可变的
list_a=[1,2,3,4,5,6]
list_a[0]=9
list_a[2:5]=[13,14,15]
print(list_a)
list_a[2:5]=[]                   #将对应元素值设置为空列表，属于切片替换，等价于del list_a[2:5]
print(list_a,len(list_a))        #需要区分=左侧的列表索引，如果是单下标(取特定值)就只是对该位置值修改
list_a=[1,2,3,4,5,6]             #当双下标时才属于切片替换，这时列表的长度会随元素删除变化
list_a[3]=[]
print(list_a,len(list_a))        #长度不变，仅把第四个元素修改为[]
list_a=[1,2,3,4,5,6]
list_a[2:5]=[None]               #长度为4，把第三个元素到第五个元素替换为了一个None元素，不包含第六个
print(list_a,len(list_a))

#当索引仅使用单下标指向单个元素时(形如list[1])，输出时才只输出该元素本身  
#当索引中使用了双下标时(形如list[1:3]/list[:3]/list[1:])，与最终指向的元素个数无关，始终输出列表格式
#例：print(list_a[1])->输出2、print(list_a[1:2])->输出[2]

#对列表截取时与字符串类似，第三个可选参数为步长，当步长参数为负数时，表示逆向截取
#该示例用于展示翻转字符串中单词顺序
def ReverseWords(input):
    inputWords=input.split(" ")    #通过空格分隔字符串，把各个单词分隔为列表
    inputWords=inputWords[-1::-1]  #参数说明:第一个参数-1表示从最后一个元素开始
    output=' '.join(inputWords)   #第二参数为空表示移动到列表开头，第三参数表示逆向步进1(向左移动1)
    return output
if __name__ =="__main__":
    input="I like runoob"
    rw=ReverseWords(input)
    print(rw)
    
#该案例中所涉及实例方法分别为str.split()和str.join()，其中split(,)的第一参数为切分依据
#向spilt中传递参数时，以参数作为指定字符对字符串进行切分
#不传递参数时按照任意空白(空格，TAB，换行)切分在不传参时也会自动去除重复空白
#第二参数为最大切分次数，通常使用read()、splitlines()读文件换行，使用rsplit()从右切分

#str.join的用法为用特定字符连接多个字符串，例如:
#"/".join(["usr","bin"])=usr/bin    "".join(["a","b","c"])=abc  "->".join(["1","2","3"])=1->2->3
#",".join("abc")=a,b,c    ",".join([1,2,3])=TypeError     ",".join(str(x) for x in [1,2,3])=1,2,3
#join()的参数必须为可迭代的字符串，如果对整数进行处理需要进行转换，如使用生成器,生成器格式如下
#join(str(x) for x in nums)
#通常使用"/".join()拼接路径、使用",".join(["",""])拼接csv行、使用"\n".join(lines)生成多行文本
#也可以使用"".join(chars)实现无分割合并

