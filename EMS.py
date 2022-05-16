# 1、显示系统的欢迎信息
print('-' * 20,'欢迎使用员工使用系统','-' * 20)

# 创建一个列表来保存员工的信息（员工的信息是以字符串的形式统一保存到列表中）
emps = ['\tnkj\t男\t21\t河北邢台','\tnhj\t男\t16\t河北邢台']

# 创建一个死循环
while True:

    # 2、用户的选择
    print('请选择要做的操作:')
    print('\t 1、查询员工')
    print('\t 2、增加员工')
    print('\t 3、删除员工')
    print('\t 4、退出')
    
    # 划分切割线
    print('-'*64)
    
    user_choose = input('请选择[1-4]:')

    # 3、根据用户的选择进行操作
    if user_choose == '1':
        # 查询员工
        # 打印表头
        print('\t序号\t姓名\t性别\t年龄\t住址')
        # 创建一个变量来保存员工的序号
        n = 1
        # 显示员工信息
        for emp in emps:
            print(f'\t{n}{emp}')
            n += 1

    elif user_choose == '2':

        # 划分切割线
        print('-'*64)

        # 添加员工
        # 获取要添加员工的信息：姓名、性别、年龄、住址
        emp_name = input('请输入员工的姓名:')
        emp_gender = input('请输入员工的性别:')
        emp_age = input('请输入员工的年龄:')
        emp_address = input('请输入员工的住址:')
        
        # 划分切割线
        print('-'*64)

        # 创建员工信息
        emp = f'\t{emp_name}\t{emp_gender}\t{emp_age}\t{emp_address}'
        
        # 显示一个提示信息
        print('员工:')
        print('\t姓名\t性别\t年龄\t住址')
        print(emp)
        user_confirm = input('将会被添加到系统中! 是否确认此操作[Y/N]:')

        # 判断是否添加员工
        if user_confirm == 'Y' or user_confirm == 'y':
            emps.append(emp)
            print('员工添加成功!')
        elif user_confirm == 'N' or user_confirm == 'n':
            print('已取消添加员工!')
        else :
            print('输入错误!!! 请输入[Y/N]')
            continue
        
    elif user_choose == '3':
        # 删除员工，根据员工的序号来删除员工
        # 根据员工的序号来删除员工
        # 获取要删除员工的序号
        del_num = int(input('请输入要删除员工的序号:'))

        # 判断序号是否有效
        if 0 < del_num <= len(emps):
            # 输入正确，根据序号获取索引
            del_index = del_num - 1
            # 显示一个提示信息
            print('员工:')
            print('\t序号\t姓名\t性别\t年龄\t住址')
            print(f'\t{del_num}{emps[del_index]}')
            user_confirm = input('将会被从系统中删除! 是否确认此操作[Y/N]:')
            
            # 判断是否删除员工
            if user_confirm == 'Y' or user_confirm == 'y':
                emps.pop(del_index)
                print('员工删除成功!')
            elif user_confirm == 'N' or user_confirm == 'n':
                print('已取消删除员工!')
            else :
                print('输入错误!!! 请输入[Y/N]')
                continue


        else :
            print('您的输入有误,请重新操作!')

    elif user_choose == '4':
        # 退出
        input('欢迎使用! 再见! 点击回车键退出')
        break
    else :
        print('您的输入有误,请重新输入!')
    
    # 划分切割线
    print('-'*64)
