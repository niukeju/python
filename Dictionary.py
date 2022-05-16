print('-'*50)

# 1、使用{}创建空字典
d = {}

# 2、给字典里添加对象
d = {'name':'nkj','age':21,'gender':'男'}
print(d,type(d))

print(d['name'],d['age'],d['gender'])

# 3、使用dict() 函数来创建字典
d = dict(name='nkj',age='21',gender='男')
print(d)

# 4、双值子序列转换为字典
dict = dict([('name','nkj'),('age','21')])
print(dict)

# 5、使用in和not in检查字典中的key
print('name' in dict)

# 6、获取字典中的值
print(dict['name'])
print(dict.get('age'))

# 7、修改字典
d['age'] = 20
print(d)

# 8、合并字典
d1 = {'a':1,'b':2,'c':3}
d2 = {'d':4,'e':5,'f':6}
d1.update(d2)
d2.update(d1)

# 9、使用len()函数获取键值对的个数
print(len(d1))

# 10、使用del来删除字典中的键值对
del d1['a']
print(d1)

#11、使用方法popitem随机删除最后一个键值对
d1.popitem()
print(d1)

# 12、使用pop删除字典中的键值对
result1 = d2.pop('d')
print(d2)
result2 = d2.pop('t','操作失败!没有此键值对')
print(result2)
print(d2)

# 13、使用clear清空字典
d.clear()
print(d)

# 14、使用copy对字典进行浅复制
c = {'name':'nkj','age':'21','gender':'男'}
c1 = c.copy()
print(c,id(c))
print(c1,id(c1))
