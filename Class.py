print('-'*50)

# 类（class）

a = int(10)         # 创建一个int类的实例
b = str('hello')    #创建一个str类的实例
print(a,type(a))
print(b,type(b))

# 1、使用class定义一个简单的类
class MyClass():
    print('This is a class')

print(MyClass)
# 使用MyClass来创建一个对象，就像调用函数一样

mc = MyClass()
mc_1 = MyClass()
mc_2 = MyClass()
# mc、mc_1、mc_2都是MyClass的实例，都是同一类对象

print('-'*50)

# 2、使用isinstance()用来检查一个对象是否是一个类的实例
i = isinstance(mc,MyClass)
print(i)

print('-'*50)

# 3、类也是一个对象，类是一个创造对象的对象
print(id(MyClass),type(MyClass))

print('-'*50)

# 4、我们可以向对象中添加变量，对象中的变量称为属性
mc.name = 'nkj'
print(mc.name)

print('-'*50)

# 5、类的定义
# 定义一个有意义的类：表示人的类
class Person:
    # 在类的代码块中，我们可以定义变量
    # 在类中我们定义的变量将会成为所有实例的公共属性
    # 所有实例都可以访问这些变量
    name = 'nkj'	# 公共属性，所有实例都可以访问
    
    # 在类中也可以定义函数，类中的定义的函数，我们称为方法
    def say_hello(a):   # 必须有a这个形参，否则运行保存
        print('你好')

# 创建Person的实例
p1 = Person()
p2 = Person()

print(p1.name)
print(p2.name)

# 调用方法：对象.方法名()
p1.say_hello()

print('-'*50)

# 6、属性和方法的查找流程
class Person:
    name = 'nkj'    # p2的name类属性值为nkj，所以p2.name输出为nkj

p1 = Person()
p2 = Person()

p1.name = 'ly'	# p1的name属性值为ly，所以p1.name输出为ly

print(p1.name)	# 调用p1.name，先在当前对象中寻找name的属性值，在7中找到了
print(p2.name)  # 调用p2.name，在当前对象中没有找到name的属性值，在类对象中找到了2

print('-'*50)

