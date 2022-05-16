print('-'*70)
# 命名空间

# 使用locals()查看全局命名空间
a = 20
s1 = locals()
print(s1,type(s1))
print(a)
print(s1['a'],type(s1['a']))

print('-'*70)

# 使用locals()查看函数命名空间
def f():
    b = 10
    s2 = locals()
    print(s2)
f()

print('-'*70)

