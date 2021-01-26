# 字符串相关demo


string = "一二三四五六七八九十"

print(string[1:4])  # 从第二位输出到第四位
print(string[0])  # 输出第一位字符
print(string[2:-1])  # 从正数第三个字符输出到倒数第二个字符、
print(string[2:])  # 从第三个字符输出到末尾
print(string[2::3])  # 从第三位开始，每隔三位输出，直到末尾
print(string * 2)  # 输出两遍
print("两只黄鹂鸣翠柳，" + string[0] + "行白鹭上青天。")  # 字符串拼接
