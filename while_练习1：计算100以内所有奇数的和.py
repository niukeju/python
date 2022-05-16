'''
练习1:
    求100以内的奇数和
'''
'''
步骤1:获取100以内的所有数
i = 0
while i < 100:
    i += 1
    print(i)

步骤2:创建一个变量保存1-100累加的和的结果
i = 0
sum = 0
while i < 100:
    i += 1
    sum += i
print(sum)

步骤3:在累加之前判断i的奇偶性
i = 0
sum = 0
while i < 100:
    i += 1
    if i % 2 != 0:
        sum += i
print(i)
'''

i = 0
sum = 0
while i < 100:
    i += 1
    if i % 2 != 0:
        sum += i
print('100以内的奇数和为:',sum)