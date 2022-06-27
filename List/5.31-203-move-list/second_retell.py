# 循环： 还是又想用 列表的指针来进行循环了 不对 这回是有内置的数据结构所以用数据结构进行循环

from typing import Dict, Optional, Union

# class ListN():
#     def __init__(val: int):
#         self.val = val

head = [1,2,3]

# test = Optional[ListN]
# 不能这样打印因为 没有输入值的地方 所以他只是起到一个检查雷丁的作用

# head 为什么返回 是这样的结构呢

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def test(head:Optional[ListNode]):
    print(head)

test(head)