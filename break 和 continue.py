'''
break 和 continue
'''
# break 可以用来立即退出循环
i = 0
while i < 5:
    if i == 2:
        break
    i += 1
    print(i)

# continue 可以跳过当次循环
j = 0
while j < 5:
    j += 1
    if j == 3:
        continue
    print(j)