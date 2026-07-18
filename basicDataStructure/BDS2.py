#列表同样可以用作队列，但由于列表的特点，直接使用列表实现队列并不是最优选择
#队列是一种先进先出(FIFO)的数据结构，意味着最早添加的元素会被最先移除
#使用列表时如果频繁地在列表的开头插入或删除元素，性能会受到影响，操作的时间复杂度是O(n)
#为了解决这个问题，python提供了collections.deque，它是双端队列，可以在两端高效地添加和删除元素
#下面是一个简单实例
from collections import deque
#初始化空队列
queue=deque()
#向队尾添加元素
queue.append('a')
queue.append('b')
queue.append('c')
print("队列状态:",queue)
#从队首移除元素
first_element=queue.popleft()
print("移除的元素:",first_element)
print("队列状态:",queue)
#查看队首元素(不移除)
front_element=queue[0]
print("队首元素:",front_element)
#检查是否为空队列
is_empty=len(queue)==0
print("队列是否为空:",is_empty)
#获取队列大小
size=len(queue)
print("队列大小:",size)

#下面是另一个仍然使用列表实现队列的实例
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from empty queue")
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("peek from empty queue")
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
# 使用示例
queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')

print("队首元素:", queue.peek())    # 输出: 队首元素:a
print("队列大小:", queue.size())    # 输出: 队列大小:3
print("移除的元素:", queue.dequeue())  # 输出: 移除的元素:a
print("队列是否为空:", queue.is_empty())  # 输出: 队列是否为空:False
print("队列大小:", queue.size())    # 输出: 队列大小:2
