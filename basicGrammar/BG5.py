#python中导入模块（外部函数）
#导入整个模块:import somemodule（模块名）
#从某个模块中导入某个函数:from somemodule import somefunction（函数名）
#从某个模块中导入多个函数:from somemodule import firstfunc,secondfunc,thirdfunc
#将某个模块中全部函数导入:from somemodule import * (不建议使用)

#导入整个模块，需要通过模块名访问模块中对象
#将整个模块作为一个对象导入到当前命名空间中，模块中对象通过module.name访问，
#不与当前命名空间中其他对象发生命名冲突


# import math
# result=math.sqrt(16)
# print(result)

#从模块中导入特定对象，使用时直接引用导入对象，无需模块名前缀
#直接将模块中对象导入到当前命名空间中，可能与当前命名空间中的其它对象发生命名冲突

# from math import sqrt
# result=sqrt(16)
# print(result)

#报错示例
#from math import sqrt
#from cmath import sqrt #复数运算的sqrt
#result=sqrt(-1) #可能会混淆使用的sqrt函数
#print(result)