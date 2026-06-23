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