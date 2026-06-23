# 标识符命名惯例：
# age = 25                # 普通变量名，最常见
# user_name = "Alice"     # 用下划线连接单词，清晰易读
# _total = 100            # 下划线开头通常表示“内部使用”或“私有”
# MAX_SIZE = 1024         # 全大写通常表示“常量”（固定不变的值）
# calculate_area()        # 函数名，动词+名词
# StudentInfo             # 类名，首字母大写（驼峰命名法）
# __private_var           # 双下划线开头，有特殊含义



#测试标识符是否合法

# def is_valid_identifier(name):
#     try:
#         exec(f"{name} = None")
#         return True
#     except:
#         return False
    
# print(is_valid_identifier("2var"))
# print(is_valid_identifier("from"))
# print(is_valid_identifier("var2"))

#使用exec()函数安全风险较高，可使用内置函数与库函数替代,如str.isidentifier()和keyword.iskeyword()

import keyword
def is_valid_identifier(name):
    return name.isidentifier() and not keyword.iskeyword(name)
print(is_valid_identifier("2var"))
print(is_valid_identifier("from"))
print(is_valid_identifier("var2"))

#python提供了keyword模块便于查询当前版本所有关键字,需要在交互编程界面查询
import keyword
keyword.kwlist