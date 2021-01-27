# number 数字练习合集
"""
Python3 支持 int、float、bool、complex（复数）。
在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
"""

print("使用内置函数 type() 可以查看变量的对象类型")
print("20 的对象类型是", type(20))
print("5.5 的对象类型是", type(5.5))
print("True 的对象类型是", type(True))
print("4 + 3j 的对象类型是", type(4 + 3j))

print("----------分割线-----------")
print("使用内置函数 isinstance () 可以判断变量的对象类型")
print(isinstance(2, float))
print(isinstance(2, int))

"""
isinstance 和 type 的区别在于：
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
"""


class A:
    a = 1


class B(A):
    a = 1


print("----------分割线-----------")
print(type(A()) == A)  # True
print(type(B()) == A)  # False
print(isinstance(A(), A))  # True
print(isinstance(B(), A))  # True

print("----------分割线-----------")
var1 = 10  # 当指定一个值时，对象就被创建
var2 = 20
var3 = 30
print(var1, var2, var3)
del var1, var2  # del 删除对象
print(var3)  # var1 和 var2 已被删除，无法输出

"""
在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。
"""
print("----------分割线-----------")
print("数值计算")
print(5 + 4)  # 9 加法
print(1.1 - 0.5)  # 0.6000000000000001 减法
print(1.5 * 3)  # 4.5 乘法
print(3 / 2)  # 1.5 除法
print(3 // 2)  # 1 除法取整
print(8 % 3)  # 2 取余
print(2 ** 3)  # 8 乘方
print(5 + True)  # 6 bool 加法  True = 1
print(5 * False)  # 0 bool 乘法  False = 0



