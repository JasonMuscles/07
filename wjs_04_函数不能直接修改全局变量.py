# 全局变量
num = 10


def demo1():

    # 希望修改全局变量的值
    # 在Python中不允许直接修改全局变量（num = 10）
    # 如果使用赋值语句智慧在函数内部定义一个局部变量
    
    num = 99

    print("demo1=》%d" % num)


def demo2():

    print("demo2=》%d" % num)


demo1()
demo2()
