def measure():
    """返回当前的温度"""

    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量结束...")

    # 在利用元组在返回温度的同时也能够返回湿度
    # 如果一个函数返回的是元组，括号可以省略
    # return (temp, wetness)
    return temp, wetness


# 元组
result = measure()
print(result)

# 需要单独处理温度或者湿度
print(result[0])
print(result[1])

# 可以使用多个变量一次接受函数的返回结果
# 使用多个变量接收结果时，变量的个数应该和元组中数据的个数一致
gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)
