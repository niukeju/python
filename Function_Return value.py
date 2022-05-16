print('-'*50)

# 1、返回值
def fr():
    return 100
r = fr()
print(r)

print('-'*50)

# 2、返回值后还可以跟函数
def f1():
    def f2():
        print('hello')
    return f2()
r1 = f1()
print(r1)    

print('-'*50)

# 3、如果仅仅写一个return，或者不写return，则相当于return None
def f3():
    return
r3 = f3()
print(r3)

print('-'*50)

# 4、在函数中，return一旦执行，函数自动结束
def f4():
    print('123')
    return
    print('abc')
print(f4())

print('-'*50)

# 5、return 和 break、continue
# 原函数
def f5():
    for i in range(5):
        print(i)
f5()
print('原函数')
print('-'*50)
# break循环
def f5():
    for i in range(5):
        if i == 3:
            break
        print(i)
f5()
print('break循环')
print('-'*50)
# continue循环
def f5():
    for i in range(5):
        if i == 3:
            continue
        print(i)
f5()
print('continue循环')
print('-'*50)
# return
def f5():
    for i in range(5):
        if i == 3:
            return
        print(i)
f5()
print('return')

print('-'*50)

# 6、使用return计算任意数的值
def sum(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result
s = sum(1,2,3)
print(s)

print('-'*50)

# 7、fn 和 fn() 的区别
def fn():
    return 10 
print(fn)
print(fn())

print('-'*50)

