#python需要注意缩进，缩进的空格数可变，但同一代码块下语句缩进必须相同

# if True:
#     print ("True")
# else:
#     print ("false")

#python中可使用反斜杠\实现多行语句
num_1 = 1
num_2 = 2
num_3 = 3
# total=num_1+num_2+num_3  #与下语句执行结果一致
# total=num_1+\
# num_2\
# +num_3
# print(total)
#在[]\{}\()中的多行语句无需使用\
total=[num_1,num_2
       ,num_3]
print(total)