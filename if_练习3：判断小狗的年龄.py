
'''
练习3:
    我家狗3岁了，5岁相当于多大年龄的人呢？
    狗的前两年每一年相当于人类的10.5岁，然后每增加一年就增加四岁。
'''

old = input('请输入狗的年龄:')
if old <= '2':
    o1 = str(int(old) * 10.5)
    print('该小狗' + o1 + '岁了')
elif old > '2':
    o2 = str((2 * 10.5) + (int(old)-2) * 4)    
    print('该小狗' + o2 + '岁了')
elif old == '0':
    print('该小狗'+ old + '岁了')
else:
    print('年龄不能为负数')