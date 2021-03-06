'''
练习一:
    打印九九乘法表
    1*1=1
    1*2=2 2*2=4
    1*3=3 2*3=6 3*3=9
    …………                9*9=81
'''

#步骤一：创建一个while外层循环控制图形的高度
i = 0
while i < 9:
    # 注意：九九乘法表是从1~9的，如果把i+=1写到最后的话就是计算0~8了
    i += 1

    #步骤二：创建一个while内层循环控制图形的高度
    j = 0
    while j < i:
        j += 1
        #步骤三：打印公式
        print('%d*%d=%d ' % (i,j,i*j),end='') 
            #end='' 表示 内部循环换行
            #字符串中使用占位符 %d--表示任意整数，（格式：%d*%d=%d,%(i,j,i*j),分别将i,j,i*j赋值给前边的%d）
    print() #print() 表示外部循环换行