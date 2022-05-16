# 函数

# 1、创建函数 def
# 创建函数的格式：
from termios import CR0


def fn():
    print('这是我的第一个函数')

# 调用函数：
fn()

print('-'*50)

# 2、形参和实参
# 定义函数指定形参
def sum(a,b):
    print(a)
    print(b)
# 调用函数时来传递实参
sum(10,20)

print('-'*50)

# 练习(1) 创建一个函数用来求任意两个数的和
def sum(a1,a2):
    print(a1 + a2)
sum(10.5,20.1)

print('-'*50)

# 练习(2) 定义一个函数，用来求任意三个数的乘积
def product(p1,p2,p3):
    print(p1*p2*p3)
product(10,2,5)

print('-'*50)

# 练习(3) 定义一个函数，可以根据不同的用户名显示不同的欢迎信息、
def welcome(w1):
    print('欢迎' + w1 + '光临')
welcome('nkj')

print('-'*50)

# 3、形参的传递方式
# 定义形参时指定默认值
def num(a,b,c = 20):
    print('a=',a)
    print('b=',b)
    print('c=',c)
num(1,2,3)

print('-'*50)

def num(a,b,c = 20):
    print('a=',a)
    print('b=',b)
    print('c=',c)
num(1,2,)

print('-'*50)

# 4、实参的传递方式
# 关键字参数
def f1(a0,b0,c0):
    print(a0,b0,c0)
f1(a0=1,b0=2,c0=3)

print('-'*50)