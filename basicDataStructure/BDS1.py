#python中数据结构通常可用列表实现，主要因为列表可变，有关列表操作方法见basicList部分
#下文为简单演示
# a=[66.25,333,333,1,1234.5]
# print(a.count(333),a.count(66.25),a.count('x'))
# a.insert(2,-1);a.append(333);print(a)
# a.index(333);print(a)
# a.remove(333);print(a)
# a.reverse();print(a)
# a.sort();print(a)
#python中，可以使用列表来实现栈的功能，栈是一种后进先出(LIFO)的数据结构，意味着最后添加的元素最先被移除
#列表提供的方法使其非常适用于栈操作，尤其是append()和pop()方法
#用append()方法可以把一个元素添加到栈顶，用不指定索引的pop()方法可以把一个元素从栈顶释放出来
#常见栈操作如下
#压入(Push):将一个元素添加到栈的顶端  弹出(Pop):移除并返回栈顶元素  获取栈的大小(Size):获取栈中元素的数量
#查看栈顶元素(Peek/Top):返回栈顶元素而不移除它  检查是否为空(isEmpty):检查栈是否为空
#以下是使用列表实现这些操作的详细说明:
stack=[]        #创建一个空栈
stack.append(1);stack.append(2);stack.append(3);print(stack)        #压入操作
top_element=stack.pop();print(top_element);print(stack)             #弹出操作
top_element=stack[-1];print(top_element)        #查看栈顶元素(不移除)
is_empty=len(stack)==0;print(is_empty)          #检查是否为空
size=len(stack);print(size)                     #获取栈的大小
#以下是一个完整示例，展示一个简单栈的实现
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
stack=Stack()
stack.push(1);stack.push(2);stack.push(3)
print("栈顶元素:",stack.peek())                #输出:栈顶元素:3
print("栈大小:",stack.size())                  #输出:栈大小:3
print("弹出元素:",stack.pop())                 #输出:弹出元素:3
print("栈是否为空:",stack.is_empty())          #输出:栈是否为空:False
print("栈大小:",stack.size())                  #输出:栈大小:2