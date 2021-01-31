# list 练习
"""
List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
"""

list1 = ["zero", 1, 2.2, "三"]
list2 = ["四", "五"]
print(list1)  # 输出完整列表
print(list1[0])  # 输出第一个元素
print(list1[1:3])  # 输出二到三
print(list1[2:])  # 输出三到末尾
print(list1 * 2)  # 输出两次列表
print(list1 + list2)  # 连接列表
print(list1[0::2])  # 隔两个输出

print((list1 * 2)[0::2])


def reverse_words(input_str):
    return "".join(input_str.split(" ")[-1::-1])


print(reverse_words("狗 是 念 来 过 倒"))





