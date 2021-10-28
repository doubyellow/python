# encoding=utf-8
import abc


# 定义一个抽象基类
class AbstractClass(metaclass=abc.ABCMeta):
    pass


# 定义一个普通类继承自object
class MyClass(object):
    pass


# 把我们定义的抽象基类注册为MyClass的父类
AbstractClass.register(MyClass)
mc = MyClass()
print(issubclass(MyClass, AbstractClass))  # 输出True
print(isinstance(mc, AbstractClass))  # 输出True

# 将我们定义的抽象基类注册到系统定义的类
AbstractClass.register(list)

print(isinstance([], AbstractClass))  # 输出True
