# 一、一切皆对象
# 二、可变对象和不可变对象
# 1.当对象的值发生变化，但内存地址没有改变时，则说明是可变类型
# 2.当对象的值发生变化，内存地址也发生改变时，则说明是不可变对象
# list,dict,set都是可变对象；int,string,tuple都是不可变对象
import sys

a = 1
b = ""
c = []
d = {}
e = lambda a:a+1
print(type(a), type(b), type(c), type(d), type(e))
print(sys.getsizeof(a), sys.getsizeof(b), sys.getsizeof(c), sys.getsizeof(d), sys.getsizeof(e))

a = {"A": 1, "B": 2}
b = a
print(id(a), id(b))
a["c"] = 3
print(id(a), id(b), a, b)
a = {"A": 1, "B": 2, "D": 3}
print(id(a), id(b), a, b)





