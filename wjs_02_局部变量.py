def demo1():

    # 定义一个局部变量
    num = 10
    print("在demo1函数内部的变量是 %d" % num)

# 函数内部定义的变量不能再其它位置使用。
# print(num)


def demo2():
    # demo1内部定义的变量不能再其它位置使用。
    # print(num)
    pass


demo1()
demo2()
