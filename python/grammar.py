
# 1 while loop 循环与判断
# while True:
#     x = input()
#     if x == 'q':
#         break
#     else:
#         print(x.upper())


# 2 try except 异常处理

# while True:
#     x = input()
#     if x == 'q':
#         break
#     try:
#         x = int(x)
#     except:
#         print(-1)
#     else:
#         print(x*5)

# 3 output python3 输出操作

# print('hello')
# print ('world')

# 4 if elif else 分支语句

# while True:
#     x = input()
#     if x == 'q':
#         break
#     y = int(x)
#     if y > 0:
#         print ('+integer')
#     elif y == 0:
#         print ('zero')
#     else:
#         print ('-integer')

# 5 for in for循环

# for x in range(10):
#     print (x*x)

# m = int(input())
# while m >0 :
#     if m % 2 == 0:
#         print (m)
#         m = m - 1
#     elif m % 3 == 0:
#         print (m)
#         m = m - 1
#         continue
#     else:
#         print('quit')
#         break

# 6 file 文件读取
# read()
# readline() 读取一行
# readlines() 一次性将文件内容读入内存，对内存不友好
# file = open('test.txt','a')
# data = "hello\n"
# file.write(data)
#
# # for line in open('test.txt', 'r').readline():
# for line in open('test.txt', 'r').readlines():
#     print(line)

# 7 range start stop step  range内置函数
# L = [x*2 for x in range(1, 7, 2)]
# print(L)

# 8 zip dict zip函数
# T1 = (1,2,3)
# T2 = (4,5,6)
#
# T = list(zip(T1,T2))
# print(T)
# D = {}
# for (k, v) in T:
#     D[k] = v
# print(D)

# 9 列表解析产生一个新的列表，编写起来更加精简，速度更快
# L = [x + 2 for x in [1,2,4]]
# print(L)


# 10 函数
# def get_no(n):
#     return n*n
#
#
# print(get_no(5))

# 11 嵌套作用域
# def maker():
#     x = 88
#
#     def more():
#         return x+1
#     return more
#
#
# f = maker()
# print(f)
# print(f())

# 12 lambda and map, 把函数作用到每一个元素

# L = [1,2,2]
#
# T = list(map(lambda x: x+3, L))
# print(T)
#
# M = [x+2 for x in L]  #列表解析
# print(M)

# 13 generator 生成器对象
# <generator object gen at 0x0000018215401BA0>
# def gen(x):
#     for i in range(x):
#         yield i+2
#
#
# X = gen(6)
# print(X)
# for i in X:
#     print(i)

# 14 返回值 函数都有返回值，如果未return，那么返回None对象
# 对应可变对象，返回值也是None

# 15 模块导入
# 搜索路径：1 主目录 2 pythonpath目录 3 标准链接库
# import mod
# from mod import *
#
# # for path in sys.path:
# #     print(path)
# # for mod in sys.modules:
# #     print(mod)
#
# mod.printer('123')
# printer('456')
# printer(dir(mod))   #模块属性信息
# printer('path:'+ mod.__file__)  #导入模块文件路径
# printer('filename:'+ mod.__name__)  #导入模块文件名称
# printer('function docstring:' + str(mod.printer.__doc__))  #函数的文档字符串

# 16 类继承，实现了高层次定制，模块与函数无法做到
# 类是产生实例的工厂
# class Animal:
#     def __init__(self, types):
#         self.types = types
#         print('p i')
#
#     def echo(self):
#         print(self.types)


# a = Animal('cat')
# a.echo()
# print(a)
#
# b = Animal('dog')
# b.echo()
# print(b)
#
# print(Animal.__dict__)


# 17 子类，超类 __init__(self,)
# class Cat(Animal):
#     """
#     This is cat class description !
#     """
#     def __init__(self, types, name):
#         self.name = name
#         super(Cat, self).__init__("data from Child") # 显式调用父类构造函数
#         print('c i')
#
#     def echo(self):
#         print('echo')
#
#
# c = Cat('cat', 'body')
# print(c.types) # data from Child
# print(c.name) # body
# print(Cat.__doc__)

# 18 装饰器 是接受了一个函数（对象），并且返回了一个函数（对象）的函数（可调用对象）
# 函数装饰器，所有函数增加公共逻辑
# 类装饰器
# def decorator(func):
#     def inner(*args, **kwargs):
#         print('before....run......')
#         res = func(*args, **kwargs)
#         print('after......run......')
#         return res
#     return inner
#
#
# @decorator
# def run():
#     print('run...............')
#
#
# run()
#
#
# class Tracer:
#     def __init__(self, func):
#         self.calls = 0
#         self.func = func
#
#     def __call__(self, *args):
#         self.calls += 1
#         print('call %s to %s' % (self.calls, self.func.__name__))
#         self.func(*args)
#
#
# @Tracer
# def spam(a,b,c):
#     print(a,b,c)
#
#
# spam(1,2,3)
# spam('a','b','c')

# 19 异常
# try except finally raise assert
# 堆栈跟踪 Traceback
# try 中没有异常发生，执行else，有异常发生不执行，有异常发生，但是except没有匹配到对应的异常，不执行
# 如果没有处理异常，则向上传递到python进程的顶层，并执行python默认的异常处理逻辑

# try:
#     a = 1/0
# except IndentationError as e:
#     print(e)
# except IndexError as e:
#     print(e)
# # except ZeroDivisionError as e:
# #     print(e)
# else:
#     print('nothing')
#
# print('continue')

# 20 内置Exception 定义异常类要继承它，是BaseException的一个子类
# BaseException 异常的顶级根类，无法被直接继承
# 定制异常类
# class MyE(Exception):
#     def __init__(self, file, line):
#         self.file = file
#         self.line = line
#
#
# try:
#     raise MyE('/etc/php.ini', 42)
# except MyE as e:
#     print('error at: file %s, line %s' % (e.file, e.line))

# 21 装饰器Decorators（函数装饰器， 类装饰器）
# 函数装饰器  是修改其他函数的功能的函数
# def wrapper(func):
#     print('exec '+str(func))
#     return func
#
#
# def hello():
#     print('hello')
#
#
# wrapper(hello)()
# # 等价于 语法糖
#
#
# @wrapper
# def world():
#     print('world')
#
#
# world()

# 22 元类 拦截并扩展类创建，提供了一种自动允许代码的方式
# 函数和类装饰器允许拦截并扩展函数调用以及类实例创建调用
