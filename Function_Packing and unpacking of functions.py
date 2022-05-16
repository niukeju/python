print('-'*50)
# 函数的装包和解包 

# 不定长参数（参数的装包）

# 在定义函数时，可以在形参前边加一个*，这样这个形参将会获取到所有的实参
# 它会将所有的实参保存到一个元组中
def f1(*a):
    print('a=',a,type(a))
f1()
f1(1,2,3)

print('-'*50)

# 练习：定义一个函数，可以计算任意数的和
def sum(*s):
    result = 0
    for r in s:
        result += r
    print(result)
sum(1,2,3)

print('-'*50)


# *形参 和 ** 形参
# * 形参只能接收位置参数，不能接收关键字参数
'''
def f2(*a):
    print('a=',a)
f2(b=1,c=2,e=3)
'''

# ** 形参可以接收位置参数，也可以接收关键字参数
def f3(**a):
    print('a=',a)
f3(b=1,c=2,d=3)

print('-'*50)

# 参数的解包
# 使用*对序列解包
# 使用fn1函数遍历元组t中的元素
# 定义fn1函数
def fn1(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)
#创建元祖t
t = (10,20,30)
# 调用函数fn1
fn1(*t)

print('-'*50)

# 使用**对字典解包
def fn2(e,f,g,h):
    print('e=',e)
    print('f=',f)
    print('g=',g)
    print('h=',h)
d = {'e':10,'f':20,'g':30,'h':40}
fn2(**d)

print('-'*50)