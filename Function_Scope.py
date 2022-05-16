print('-'*50)
# 作用域（scope）
# 全局作用域 和 函数作用域
# 1、全局作用域

a = 10  # 全局变量

def f():
    b = 20  # 定义在函数内部，所以它的作用域是函数内部
    print('a=',a)
    print('b=',b)
f()

print('a=',a)

print('-'*50)

# 2、函数作用域

a = 10  # 全局变量

def f():
    b = 20  # 函数变量
    print('a=',a)
    print('b=',b)
f()
f()
f()
# f() 被调用了三次，所以产生了三个函数作用域

print('a=',a)

print('-'*50)

# 查找顺序
d = 20
def f0():
    def f1():
        d = 10
        print('d=',d)
    f1()
f0()

print('-'*50)

d = 20
def f0():
    def f1():
        print('d=',d)
    f1()
f0()

print('-'*50)

