# 遍历字典

# 1、通过keys()遍历获得key
d = {'name':'nkj','age':'21','gender':'男'}
a = d.keys()
for k in a:
    print(k)

print('-'*50)

# 2、通过keys()遍历获得value
d = {'name':'nkj','age':'21','gender':'男'}
for i in d.keys():
    print(d[i])

print('-'*50)

# 3、通过values()遍历字典中的值
d = {'name':'nkj','age':'21','gender':'男'}
for v in d.values():
    print(v)

print('-'*50)

# 4、使用items()遍历字典中所有的值
d = {'name':'nkj','age':'21','gender':'男'}
for i in d.items():
    print(i)

d = {'name':'nkj','age':'21','gender':'男'}
for k,v in d.items():
    print(k,'=',v)

print('-'*50)