#python中数字只有四种类型：int（无long，直接表示为长整型）、bool(True/False)、
#float（1.23、3E-2）、complex（形式如a+bj、a为实部，b为虚部，j表示虚数单位）
#python中单引号和双引号使用相同，使用三引号（'''或"""）可指定一多行字符串
#反斜杠\可用于转义，增加r可让反斜杠不转义直接输出
print("this is a line with\n")
print(r"this is a line with\n") 
#字符串可用+运算符连接，用*重复,重复输出时print不自动换行
print("this""is""a""line")
print("this"+"is"+"a"+"line")
print("this is a line "*3)
#python中字符串有两种索引，从头开始索引以0开始，从尾部开始索引以-1开始（倒数第一个是-1，以此类推）
#python中字符串无法改变，且没有单独字符类型，一个字符就是长度为1的字符串
#字符串切片str[start:end:step]，start（包含）为开始索引，end（不包含）为结束索引，step为步长参数
str="123456789"
print(str[0:-1])    #取第一个到倒数第二个，倒数第一个不包含 ==str[0:8]
print(str[0:8])    
print(str[0:-1:2])  #取第一个到倒数第二个，步长为2（间隔为1）
print(str[2:])      #取第三个到最后一个
print(str[:-3])     #取第一个到倒数第四个
print(str[-3:])     #取倒数三位，用于提取域名后缀
print(str+' nihao')