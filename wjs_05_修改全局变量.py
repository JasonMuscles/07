# 全局变量
num = 10


def demo1():
    # 希望修改全局变量的值 - 使用global声明一下变量即可
    # global 关键字，告诉 Python 解释器 num 是一个全局变量
    global num

    num = 99

    print("demo1=》%d" % num)


def demo2():
    print("demo2=》%d" % num)


demo1()
demo2()
