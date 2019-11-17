# 在开发时要将全局变量定义在最上方便于正常访问
num = 10


def demo():

    print("%d" % num)
    print("%s" % title)
    print("%s" % name)


# 再定定义一个全局变量
title = "Jason"

demo()

# 在定义一个全局变量
# name = "小明"
