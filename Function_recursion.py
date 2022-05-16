print('-'*70)
# 递归

# 1、练习
# 计算10的阶乘（10！）
# 方法一：
a = 1*2*3*4*5*6*7*8*9*10
print(a)

print('-'*70)

# 方法二：for循环
n = 10                  # 求10个阶乘，n=10
for i in range(1,10):   # 遍历1~10
    n *= i              # n = n * i

print(n)            # 输出n的值

print('-'*70)

# 方法三：使用函数求10的阶乘
def f(n): 
    '''
    该函数用于求任意数的阶乘
    参数：
        n -- 要求阶乘的数字
    '''
    # 创建一个变量来保存结果
    result = n

    for i in range(1,n):
        result *= i
        
    return result
print(f(20))

print('-'*70)

# 2、递归函数
# 无穷递归：如果这个函数被调用，程序内存会溢出，效果类似于死循环
def f():
    f()

# 3、使用递归函数求任意数的阶乘
def f0(n):
    '''
    该函数用于求任意数的阶乘
    参数：
        n -- 表示任意数
    '''
    
    # 基线条件：当n为1时，递归不再继续
    if n == 1:
        # 1的阶乘就是1，直接返回1
        return 1

    # 递归条件：n = n * (n-1)!
    return n * f0(n-1)

print(f0(10))

print('-'*70)

# 4、递归练习
# (1) 创建一个函数 power 来为任意数字做幂运算
# 方法一：
def power1(x,y):
    '''
    power()函数用来求任意数的幂运算
    参数：
        x -- 底数
        y -- 指数
    '''
    return x ** y
print(power1(2,3))

print('-'*70)

# 方法二：
def power2(q,w):

    # 基线条件
    if w == 1:
        return q
    # 递归条件
    return q * power2(q,w-1)
print(power2(3,5))

print('-'*70)

# (2) 创建一个函数，用来检查一个任意的字符串是否为回文字符串(abcba),如果是则返回True，不是则返回False
def huiwen(e):
    '''
    这是一个判断字符串是否为回文字符串的函数，
    如果是回文字符串,返回True;
    如果不是回文字符串,返回False
    '''
    # 先检查第一个字符串和最后一个字符串是否一致
    # 基线条件:字符串长度小于2时，字符串一定为回文字符串
    if len(e) < 2:
        return True
    elif e[0] != e[-1]:
        return False

    # 递归条件
    return huiwen(e[1:-1])  # 切片[a,b] -- 包括a,不包括b

print(huiwen('abcdcba'))

# 或者
def huiwen(e):
    if len(e) < 2:
        return True
    return e[0] == e[-1] and huiwen(e[1:-1]) 
print(huiwen('abcdcba'))

print('-'*70)
