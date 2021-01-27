# print 输出相关练习

x = "中国"
y = "北京"
print(x)
print(y)
print("----------分割线-----------")
print(x, y)  # sep 用于在字符串之间插入字符，默认为空格
print(x, y, sep=",")  # sep 用于在字符串之间插入字符，默认为空格
print("----------分割线-----------")
print(x, y)  # end 用于在末尾添加字符。默认为换行
print("** 无用的空行 **")
print(x, y, end=" 王府井 ")  # end 用于在末尾添加字符。默认为换行
print("** 无用的空行 **")
print("----------分割线-----------")
print(x, file=open("files/printFile.txt", mode="w", encoding="utf-8"))  # file 用于把指定文本发送到文件中，mode=w是写，这里指定编码为utf-8
