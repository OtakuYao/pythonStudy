# tuple 元组练习

"""
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
"""

my_tuple = ('apple', 786, 2.23, 'orange', 70.2)
tiny_tuple = (123, 'pen')

print(my_tuple)  # 输出完整元组
print(my_tuple[0])  # 输出元组的第一个元素
print(my_tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(my_tuple[2:])  # 输出从第三个元素开始的所有元素
print(tiny_tuple * 2)  # 输出两次元组
print(my_tuple + tiny_tuple)  # 连接元组
