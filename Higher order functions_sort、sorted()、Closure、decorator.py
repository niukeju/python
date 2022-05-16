# 高阶函数_sort、闭包、解释器

print('-'*70)

# 1、sort -- 该方法用于对列表中的元素进行排列
s1 = ['bb','dddd''aaa','c']
s1.sort()
print(s1)

# sort()中可以接收一个关键字参数 key
s1 = ['bb','dddd''aaa','c']
s1.sort(key=len)
print(s1)

# 使用sort(key=?)对不同类型的元素进行排序
s1 = [1,2,'3','4',5,'6',7,'8']
s1.sort(key=int)
print(s1)
s1 = [1,2,'3','4',5,'6',7,'8',9,10]
s1.sort(key=str)
print(s1)

# sorted()函数
# sorted()函数和sort()方法的用法基本一致，sorted()函数可以对任意的序列进行排序，而且使用sorted()不会影响原来的对象，而是会返回一个新对象
s1 = ['2',1,3,'4',5,'9',6,'8']
sorted(s1,key=int)
print(s1)

print('-'*70)

# 2、闭包
# 将函数作为返回值返回
def f():
    # 函数内部再定义一个函数

    a = 10

    def inner():
        print('这是f()内部的inner()函数',a)
        print(a)
    
    # 将内部函数 inner 作为返回值返回
    return inner

# i是一个函数，是调用f()后返回的函数
# i定义在函数内部，不是全局函数，所以这个函数总能访问到f()函数内的变量
i = f()
i()
print(i)

print('-'*70)

# 闭包练习
# 求多个数的平均值
# 方法一：用最简单的方法求平均值
num = [10,20,30,40,50]
# 使用sum()求num中几个数的和
print(sum(num)/len(num))

print('-'*50)

# 方法二：使用函数求平均值
# 创建一个列表，用于保存数值
num = []
# 创建函数，求平均值
def average(n):
    # 将n添加到列表num中
    num.append(n)
    # 求平均值
    return sum(num)/len(num)
# 调用函数，求平均值
print(average(10))
print(average(20))
print(average(20))
# 注意：num列表是用来保存求平均值获得的参数的，如果被别人修改则会丢失，所以要将num列表做成闭包

print('-'*50)

# 方法三：将num列表进行闭包，求平均值
def make_average():
    num = []
    def average(n):
        num.append(n)
        return sum(num)/len(num)
    return average

average = make_average()
print(average(10))
print(average(20))


print('-'*70)

# 3、装饰器
# 创建几个函数
# 求任意两个数的和
def add(a,b):
    '''
    求任意两个数的和
    '''
    print('计算开始……')
    r = a + b
    print('计算结束……')
    return r
print(add(10,20))

print('-'*30)

# 求任意两个数的乘积
def mul(a,b):
    '''
    求任意两个数的乘积
    '''
    print('计算开始……')
    m = a * b
    print('计算结束……')
    return m
print(mul(10,20))

print('-'*50)

# 以上我们可以直接通过修改函数中的代码来完成这个需求，但是会产生以下一些问题如果要修改的函数过多：	
# 1.修改起来会比较麻烦
# 2.不方便后期的维护
# 3.会违反开闭原则（OCP原则）
#      OCP原则：程序的设计，要求开发对程序的扩展，要关闭对程序的修改
# 我们都希望在不改变程序扩展的情况下，对函数进行扩展，只需要现有的函数，再创建一个函数
def f0():
    print('这是f0()函数')

def f1():
    print('函数开始运行……')
    f0()
    print('函数运行结束……')

f1()

print('-'*50)

# 例：对上面的add()函数进行扩展
# 普通函数
# 求任意两个数的和
def add(a,b):
    '''
    求任意两个数的和
    '''
    print('计算开始……')
    r = a + b
    print('计算结束……')
    return r

# 对上面普通函数进行扩展
def new_add(a,b):
    print('计算开始……')
    a0 = add(a,b)
    print('计算结束……')
    return a0
na = new_add(10,20)
print(na)

print('-'*50)

# 该方法还有一个问题：太麻烦，对几个函数扩展就需要重新定义几个函数
# 为了解决这个问题，我们创建一个自动帮我们生产函数函数

# 定义一个函数
def begin_end(old):
    '''
    此函数用于帮我们创建其他函数的扩展函数
    参数：
        old -- 要扩展的函数对象
    '''
    # 创建一个新函数
    def new_function(*t,**d):   # 将未知参数或者关键字参数装包成元组或者字典
        print('开始执行……')
        # 调用被扩展的函数
        old(*t,**d)             # 将元组或者字典拆包成未知参数或者关键字
        print('执行结束……')

    # 返回这个新函数
    return new_function

fun = begin_end(f0)
fun()

@ begin_end
def say_hello():
    print('hello，大家好！')

say_hello()

print('-'*70)