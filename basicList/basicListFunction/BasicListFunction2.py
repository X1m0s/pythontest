#-----6.insert()-----
#该函数用于将指定对象插入列表中指定位置，list.insert(index,obj)中index为对象obj插入的索引位置
list1=["Google","Runoob","Taobao"]
list1.insert(1,"Baidu")
print("列表插入元素后为:",list1)
#-----7.reverse()-----
#该函数用于反向处理列表中元素
list1=["Google","Runoob","Taobao","Baidu"]
list1.reverse()
print("列表反转后:",list1)
#-----8.sort()-----
#该函数用于对原列表进行排序,会修改原列表排列顺序
#list.sort(key,reverse),key为对元素排序前调用的函数，reverse为升序/降序排列，当True时降序否则升序
lista=[3,1,4,1,5];lista.sort()                              #默认升序排列
print(lista)    
lista=[3,1,4,1,5];lista.sort(reverse=True)                  #降序排列
print(lista)
lista=["Banana","apple","Cherry"];lista.sort(key=str.lower) #全转换为小写字符后升序排列
print(lista)
lista=["dog","elephant","Bird","CAT"];lista.sort(key=len)   #根据长度升序排列
print(lista)
lista=[3,1,4,1,5]
listb=sorted(lista) 
print(f"lista={lista},listb={listb}")                   #用于区分sorted()和list.sort()
lista.sort()                                            #sort()原地修改返回None，sorted返回新列表
print(f"lista.sort()={lista}")                          #sorted()不修改原列表，list.sort()修改原列表
#通过自定义函数排序列表示例如下
def getSecond(lst):
    return lst[1]
list_test=[(1,4),(3,2),(2,3),(4,1),(0,5),(5,0)]
list_test.sort()
print("list_test普通升序排列结果为:",list_test)         #比较序列时按照字典序比较
list_test.sort(key=getSecond)
print("list_test使用第二个元素排列结果为:",list_test)
#-----9.clear()-----
#该函数用于清空列表，效果类似于del a[:]
list1=["Google","Runoob","Taobao","Baidu"]
list1.clear()
print("列表清空后:",list1)
#-----10.copy()-----
#该函数用于复制列表，效果类似于a[:]，返回值为复制后的新列表(但内部元素仍是原对象的引用)
list1=["Google","Runoob","Taobao","Baidu"]
list2=list1.copy()
print("list2=",list2)
