my_list = [] # 空列表

my_list = [528] # 创建一个只包含一个元素的列表

my_list = [10,'hello',True,False,[1,2,3],print] # 列表中可以存储任意的对象


my_list = [1,2,3,2,3,2,4,2,5,2]

print(my_list.index(2,2,4)) #表示从列表的第2位置开始查找“2”在列表中的位置，到4的位置结束查找

print(my_list.count(2)) # 查找列表中“2”的个数


# ⭐修改列表
my_list = [1,2,3,4,5,6]

# 通过索引修改列表
my_list[0] = 'nkj'
print('通过索引index修改列表:',my_list)

# 删除列表中的元素
del my_list[0]
print('使用del删除列表中的元素:',my_list)

# 通过切片修改列表
my_list[:2] = 'nkj'
print('使用切片修改列表后的结果:',my_list)

# 通过方法来修改列表
# 1、append() -- 插入
my_list.append('7')
print('使用 append() 方法修改后的列表:',my_list)

# 2、insert() -- 在指定位置添加元素
my_list.insert(0,'nkj')
print('使用 insert() 方法在列表的指定位置添加元素:',my_list)

# 3、extend() -- 使用新的序列来扩展当前序列
my_list.extend(['n','k','j'])
print('使用 extend() 方法来扩展序列:',my_list)

# 4、clear() -- 清空序列
# my_list.clear()
# print('使用 clear() 方法清空序列:',my_list)

# 5、pop() -- 根据索引删除指定元素并返回到指定元素
my_list.pop(0)
print('使用 pop() 方法删除索引的指定元素:',my_list)

# 6、remove() -- 删除指定值的元素
my_list.remove(5)
print('使用 remove() 方法删除指定值的元素:',my_list)

# 7、reverse() -- 反转列表
my_list.reverse()
print('使用 reverse() 方法反转列表:',my_list)

# 8、sort() -- 对列表进行升序排列
#    sort(reverse = True) -- 对列表进行降序排列
my_list1 = [89,45,3,6,2,8,1,3,8,10]
my_list1.sort()
print('使用 sort() 方法对列表进行升序排列 : ', my_list1 )

my_list2 = ['dnklgkjbugha']
my_list2.sort(reverse = True )
print('使用 sort(reverse = True) 方法对列表进行降序排列 : ', my_list2 )
