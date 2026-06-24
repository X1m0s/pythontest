#-----8.max()&min()-----
#该函数为内置函数，无需导入外部模块
#max()和min()函数各项属性均相同，仅功能不同，不做重复描述
#max()函数的参数列表为max(参数1,参数2,...,key)，其中key的默认值为None，为比较前对元素调用的函数
print("max(1,5,3)=",max(1,5,3)," min(1,5,3)=",min(1,5,3),sep="")
print("max('a','z','m')=",max('a','z','m')," min('a','z','m')=",min("a","z","m"),sep="")
#函数中的参数key函数仅在比较前进行调用，不会修改max比较的参数值本身，仍然按调用前参数输出结果
print("max(-1,-5,3)=",max(-1,-5,3,key=abs)," min(-1,-5,3)=",min(-1,-5,3,key=abs),sep="")
print("max(['abc', 'a', 'ab'], key=len)=",max(["abc", "a", "ab"], key=len))
#max()函数的另外一种参数情况为max(可迭代对象1,可迭代对象2...,key,default)
print("max('hello')=",max("hello")," min('hello')=",min("hello"),sep="")
#当比较参数为字符时，按字母顺序作为大小排序
print("max([])=",max([],default=0))
#default为可迭代对象为空时的返回值，此外比较的可迭代对象最好为单个，函数要求所有参数同类型
#参数中可以为全Number(数字)，或者为全Sequence(序列)，但不同长度的列表可按字典序比较
print("max([1,2],[3])=",max([1,2],[3]))
#当比较多个可迭代对象(容器)时，逐个元素对比,当比较出大小时停止，此时返回值为序列，例如
print("max([1,9],[2,1])=",max([1,9],[2,1]))
print("max([1,2],[1,1])=",max([1,2],[1,1]))
#当比较结果完全一致时，返回最先遇到的元素
print("max('Aa','aA',key=str.lower)=",max("Aa","aA",key=str.lower))

"""
字典序示例
列表比较如同比单词
[1, 2, 3] < [1, 2, 5]   # True   前两位相同，第三位 3<5
[1, 9]    > [1, 2, 3]   # True   第二位 9>2,后面不用看
[1, 2]    < [1, 2, 3]   # True   前缀相同，短的更小
[1, 2]    > [1, 3]      # False  第二位 2<3
字符串同理
"abc" < "abd"     # True   前两位相同,c < d
"ab"  < "abc"     # True   短的小
"apple" < "app"   # False  l > (空)
"""
#-----9.modf()-----
import math
print("math.modf(100.12)=",math.modf(100.12))      #modf()函数在math模块下,同样仅支持实数参数
print("math.modf(-100.72)=",math.modf(-100.72))    #modf()返回参数的整数部分和小数部分
print("math.modf(119)=",math.modf(119))            #modf()返回值为浮点型元组
print("math.modf(math.pi)=",math.modf(math.pi))    #元组的第一个元素为小数部分，第二个为整数部分
#-----10.pow()-----
#pow()函数较为特殊，python内置的pow()函数参数值为pow(x,y,z)，使用方式是计算x的y次方
#如果存在z对结果取模，等效于x**y%z，math模块的pow()函数仅支持(x,y)两个参数，此外会将参数转换为浮点型
print("math.pow(100,2)=",math.pow(100,2))
print("pow(100,2)=",pow(100,2))
print("math.pow(100,-2)=",math.pow(100,-2))
#内置的pow()函数支持复数计算，但不支持参数z的对结果取模
print("pow(3+2j,2)=",pow(3+2j,2))
#-----11.round()-----
print("round(70.23456)=",round(70.23456))           #round()函数为内置函数，用于返回浮点数的四舍五入值
print("round(56.659,1)=",round(56.659,1))           #参数列表为round(x,n)，n为精确到小数点后位数
print("round(80.264,2)=",round(80.264,2))
print("round(100.000056,3)=",round(100.000056,3))
print("round(-100.000056,3)=",round(-100.000056,3))
#个别情况下返回结果不正确，主要原因是浮点数精度问题
#-----12.sqrt()-----
print("math.sqrt(100)=",math.sqrt(100))             #sqrt()函数在math模块下，仅支持实参，返回值为浮点
print("math.sqrt(7)=",math.sqrt(7))                 
print("math.sqrt(math.pi)=",math.sqrt(math.pi))