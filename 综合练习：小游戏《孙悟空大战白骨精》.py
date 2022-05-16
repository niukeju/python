'''
if、while、循环嵌套，三者综合练习:小游戏《西游记大战BOSS》
'''
'''
游戏逻辑步骤:

步骤1:身份选择
    1、显示提示信息
        欢迎光临 XXX 游戏 !
        请选择你的身份:
            ①、XXX
            ②、XXX
        请选择:X
    2、根据用户选择来分配身份，选择身份之后会有提示信息:
        ①、---
        ②、---
        ③、---
步骤2:游戏进行
    1、显示玩家的基本信息属性（攻击力、防御力、生命值）
    2、显示玩家可以进行的操作（练级、打BOSS、逃跑）
        ①、练级 -- 提高玩家的英雄属性
        ②、打BOSS -- 玩家攻击BOSS，同时BOSS对玩家进行反击
                        -- 计算BOSS是否被玩家消灭，同时计算玩家是否被BOSS消灭
                 -- 游戏结束
        ③、逃跑 -- 退出游戏，提示信息:游戏结束!
'''

# 步骤一、身份选择

# 1、显示欢迎信息
print('-'*20 + '欢迎来到《西游记大战BOSS》' + '-'*20)

# 2、显示身份选择的信息
print('请从以下选择你的身份:')
print('\t 1、孙悟空')
print('\t 2、猪八戒')
print('\t 3、白骨精') # "\t"表示缩进

# 3、创建变量，保存用户所选的角色->孙悟空<-的属性（攻击力、防御力、生命值）
play_attack_1 = 10 # 攻击力
play_life_1 = 100 # 生命值

# 创建变量，保存用户所选的角色->猪八戒<-的属性（攻击力、防御力、生命值）
play_attack_2 = 5 # 攻击力
play_life_2 = 150 # 生命值

# 创建变量，保存反派BOSS的属性（攻击力、防御力、生命值）
play_attack_3 = 10 # 攻击力
play_life_3 = 100 # 生命值

# 创建变量，保存用户所选的角色->白骨精<-的属性（攻击力、防御力、生命值）
play_attack_4 = 1 # 攻击力
play_life_4 = 10 # 生命值

# 4、用户游戏身份的选择 (创建 变量 play_choose 保存用户所选择的身份)
play_choose_1 = input('请选择你的身份[1-3]:')

# 分割线
print('-'*70)

# 5、使用if语句来对用户进行信息提示 以及 玩家所选角色的信息
if play_choose_1 == '1':
    print('你选择了1，你将以->孙悟空<-的身份来进行游戏!')
    print(f'孙悟空，你的攻击力是{play_attack_1},你的生命值是{play_life_1}')

elif play_choose_1 == '2':
    print('你选择了2，你将以->猪八戒<-的身份来进行游戏!（这个角色适合淼举来玩[偷笑]）')
    print(f'猪八戒，你的攻击力是{play_attack_2},你的生命值是{play_life_2}')
    # 格式化字符串：“ f'字符串语句{变量}' ”

elif play_choose_1 == '3':
    print('你选择了3，你竟然选择了坏蛋，你将会收到惩罚')
    print(f'惩罚就是:白骨精，你的攻击力是{play_attack_4},你的生命值是{play_life_4}')

else :
    print('请从[1-3]中选择角色!')

# 步骤二、进入游戏，游戏进行

# 注意：游戏选项是需要重复显示的，所以必须将其写到一个循环中
# 无限循环；"while True"
while True:

    #分割线
    print('-'*70)

    # 1、显示游戏选项，游戏正式开始
    print('请选择你要进行的操作:')
    print('\t 1、打副本升级')
    print('\t 2、直接打BOSS')
    print('\t 3、逃跑')
    play_choose_2 = input('请选择你要做的操作[1-3]:')

    # 使用if语句对用户的选择进行处理

    # 玩家选择 “1、打副本升级”：
    if play_choose_1 == '1' and play_choose_2 == '1' :
        play_attack_1 += 2
        play_life_1 += 2
        print('-'*70)
        print('孙悟空，恭喜你! 刷副本升级完成! 你的攻击力增加为:',play_attack_1)
        print('孙悟空，恭喜你! 刷副本升级完成! 你的生命值增加为:',play_life_1)
        print('-'*70)
    elif play_choose_1 == '2' and play_choose_2 == '1' :
        play_attack_2 += 2
        play_life_2 += 2
        print('-'*70)
        print('猪八戒，恭喜你! 刷副本升级完成! 你的攻击力增加为:',play_attack_2)
        print('猪八戒，恭喜你! 刷副本升级完成! 你的生命值增加为:',play_life_2)
    elif play_choose_1 == '3' and play_choose_2 == '1':
        print('你所选的角色是白骨精，不能打怪升级!!!')

    # 玩家选择 “2、直接打BOSS”：

    
        print('-'*70)

    # 攻击BOSS的步骤：
        # 1、玩家1攻击BOSS
    elif play_choose_1 == '1' and play_choose_2 == '2' :
        play_life_3 -= play_attack_1

        print('-'*70)
            # 判断BOSS是否死亡
        if play_life_3 <= 0 :
            print('BOSS死亡!!! 你取得了胜利! 游戏结束!!!')
        else:
            print(f'BOOS受到了{play_attack_1}点的攻击，BOSS剩余的血量为:{play_life_3}')

        # 2、BOSS反击玩家1
            play_life_1 -= play_attack_3
            print(f'你被BOSS击中，受到了{play_attack_3}的伤害，剩余血量:{play_life_1}')
            if play_life_2 <= 0:
                print('你被BOSS打死了! 游戏结束!!!')
                print('-'*70)
                break

        # 3、玩家2攻击BOSS
    elif play_choose_1 == '2' and play_choose_2 == '2' :
        play_life_3 -= play_attack_2

        print('-'*70)
            # 判断BOSS是否死亡
        if play_life_3 <= 0 :
            print('BOSS死亡!!! 你取得了胜利! 游戏结束!!!')
        else:
            print(f'BOOS受到了{play_attack_2}点的攻击，BOSS剩余的血量为:{play_life_3}')

        # 4、BOSS反击玩家2
            play_life_2 -= play_attack_3
            print(f'你被BOSS击中，受到了{play_attack_3}的伤害，剩余血量:{play_life_2}')

            if play_life_2 <= 0:
                print('你被BOSS打死了! 游戏结束!!!')
                print('-'*70)
                break

        # 5、玩家3攻击BOSS
    elif play_choose_1 == '3' and play_choose_2 == '2' :
        play_life_3 -= play_attack_4
        
        print('-'*70)
            # 判断BOSS是否死亡
        if play_life_3 <= 0 :
            print('BOSS死亡!!! 你取得了胜利! 游戏结束!!!')
        else:
            print(f'BOOS受到了{play_attack_4}点的攻击，BOSS剩余的血量为:{play_life_3}')

        # 6、BOSS反击玩家2
            play_life_4 -= play_attack_3
            print(f'你被BOSS击中，受到了{play_attack_3}的伤害，剩余血量:{play_life_4}')

            if play_life_4 <= 0:
                print('你被BOSS打死了! 游戏结束!!!')
                print('-'*70)
                break
    
    elif play_choose_2 == '3':
        print('你已经逃跑!!! 怂包! 游戏结束!!!')
        break
    

        