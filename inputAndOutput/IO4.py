#-----5.f.tell()-----
#f.tell()用于返回文件当前的读/写位置(即文件指针的位置)。文件指针表示从文件开头开始的字节数偏移量。
#f.tell()返回一个整数，表示文件指针的当前位置

#-----6.f.seek()-----
#如果需要改变文件指针当前位置，可以使用f.seek(offset,whence)把指针移动到指定位置
#offset表示相对于whence参数的偏移量，whence的值如果是0表示开头，1表示当前位置，2表示文件尾
#例如：
#seek(x,0):从起始位置即文件首行首字母开始移动x个字符
#seek(x,1):表示从当前位置往后移动x个字符
#seek(-x,2):表示从文件的结尾往前移动x个字符
#whence的值默认为0，即文件开头，下面是一个实例
f=open('tmp/foo2.txt','rb+')
print(f.write(b'0123456789abcdef'))
print(f.seek(5))
print(f.read(1))
print(f.seek(-3,2))
print(f.read(1))

#-----7.f.close()-----
#在文本文件中(打开时没有使用b来按二进制格式打开的)，只会相对于文件起始位置定位
#在处理完文件后，调用f.close()关闭文件并释放系统资源，如果再尝试调用文件则会抛出异常
#因此在处理文件对象时，使用with关键字是一个良好的方式，在结束后会帮你正确关闭文件

#python的pickle模块实现了基本的数据序列和反序列化
#通过pickle模块的序列化操作能将程序中运行的对象信息永久存储到文件中
#通过pickle模块的反序列化操作，可以从文件中创建上一次程序保存的对象
#基本接口:pickle.dump(obj,file,[,protocal])
#有了pickle对象，就可以对file以读取的形式打开:
#x=pickle.load(file)    从file(类文件对象，有read()和readline()接口)中读取一个字符串，并将它重构为原来的python对象
import pickle
data1={'a':[1,2.0,3,4+6j],
       'b':('string',u'Unicode String'),
       'c':None}
selfref_list=[1,2,3]
selfref_list.append(selfref_list)
output=open('tmp/data.pkl','wb')
pickle.dump(data1,output)
pickle.dump(selfref_list,output,-1)
output.close()

import pprint
pkl_file=open('tmp/data.pkl','rb')
data1=pickle.load(pkl_file)
pprint.pprint(data1)
data2=pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()

#针对序列化，简单来说就是将内存中的对象转写成字节流，存到磁盘，反序列化就是从磁盘重新读回内存
#使用二进制模式是因为pickle输出的是字节流而非文本
#dump()函数中的参数protocal常见的取值为(0:ASCII协议 1/2/3:旧版二进制协议 4:Python3.4+ 5:Python3.8+ -1:自动选当前Python支持的最高版本)
#pickle可以存储任何python的内置类型，甚至是自定义类实例和自引用
#dump和load是按顺序一一对应的，每个dump()都会在文件中加一段，每个load()都会读取一段，先存先读(类似FIFO?)
#pprint()比起print()输出挤在一行，pprint.pprint()会格式化展开，可以更清晰体现嵌套结构
#总结：
#pickle 就像记忆卡存档——不管程序里的对象结构多复杂，dump() 存盘、load() 读回来，完美还原。
#唯一要注意的就是：只从可信来源读取，因为加载 pickle 可以执行任意代码，有安全风险。