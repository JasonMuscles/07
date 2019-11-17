# 在开发时要将全局变量定义在最上方便于正常访问
gl_num = 10
# 再定定义一个全局变量
gl_title = "Jason"
# 在定义一个全局变量
gl_name = "小明"


def demo():

    num = 99

    print("%d" % num)
    print("%s" % gl_title)
    print("%s" % gl_name)


demo()

