# 遍历列表 -- 指的是将列表中的所有元素全部取出来 
list = [1,2,3,4,5]

# 1、遍历列表最简单的方式
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])

 
# 2、通过while循环来遍历列表
i = 0
while i < len(list): # len()函数可以计算出列表的长度
    print(list[i])
    i += 1


# 3、通过for循环来遍历列表

#for语句语法:
#    for 变量 in 序列:
#        循环体(代码块)

for l in list:
    print(l)
# for循环的代码块会执行多次，列表中有多少个元素for循环就会执行多少次
# 每执行一次就会将序列中的一个元素赋值给变量，所以我们可以用变量来遍历列表中的元素

