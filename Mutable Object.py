# 可变对象

print('-'*70)
# 1、修改对象 -- 对象的值改变，id不变
a = [1,2,3]
a[0] = 10
print('a=',a,id(a))

# 修改变量 -- 将对象重新赋值，值和id都改变
a = [4,5,6]
print('a=',a,id(a))

print('-'*70)

# 2、修改对象c后，b的值和id都会发生变化
b = [1,2,3]
c = b
c[0] = 10
print('b=',b,id(b))
# 对c修改变量后，b的值变化，id不变
b = [1,2,3]
c = [4,5,6]
print('b=',b,id(b))

print('-'*70)

# 3、== 和 is
# == 和 != 比较的是对象的值
e = [1,2,3]
f = [1,2,3]
print(e == f)

# is、is not 比较的是对象的id
print(e is f)

print('-'*70)