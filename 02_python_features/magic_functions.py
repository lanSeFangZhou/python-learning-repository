# 三、隐藏的方法和属性
# def __init__(self):通常用于初始化一个新实例，控制这个初始化的过程，比如添加一些属性， 做一些额外的操作，发生在类实例被创建完以后
#
# def __new__(self):通常用于控制生成一个新实例的过程。它是类级别的方法
#
# def __str__(self):如果要把一个类的实例变成 str，就需要实现特殊方法
#
# def __repr__(self):它是一个 ”自我描述“ 的方法，此方法通常实现这样的功能： 当直接打印类的实例化对象时，系统将会输出对象的自我描述信息，用来告
# 诉外界对象具有的状态信息。
#
# def __dict__(self):包存了类或对象内部所有属性和方法对应的字典
#
# def __getattr__(self,name):类不存在该属性时__getattr__函数会被激活
#
# def __getattribute__(self,name):是属性访问拦截器，就是当这个类的属性被实例访问时，会自动调用类的__getattribute__方法
#
# def __setattr__(self,name,value):在类实例的每个属性进行赋值时，都会首先调用__setattr__()方法，并在__setattr__()方法中将属性名和属性
# 值添加到类实例的__dict__属性中
#
# def __delattr__(self,name):不建议大家直接调用__delattr__方法来删除实例的属性，不过在特定情况下可以通过重写该方法进行一些属性删除的特殊处
# 理，确保相关实例属性释放时程序进行了正确处理
#
# def __call__(self,arg,**key):自定义函数的调用，通常情况下是在函数名后加()来调用。但同样也可以用__call__()方法来调用

class Magic_Functions():
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __dict__(self):
        pass

    def __getattr__(self, item):
        pass

    def __getattribute__(self, item):
        pass

    def __setattr__(self, key, value):
        pass

    def __delattr__(self, item):
        pass

    def __call__(self, *args, **kwargs):
        pass
    