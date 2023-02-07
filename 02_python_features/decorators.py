# 装饰器的作用就是为已经存在的对象添加额外的功能
# 内置的装饰器有三个，分别是staticmethod、classmethod和property，作用分别是把类中定义的实例方法变成静态方法、类方法和类属性。

import time

def timeit(func):
    def wrapper():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        print(f"used:{end - start}")
    return wrapper

@timeit
def foo():
    print("in foo()")

foo()