def add(a, b):
    # Bug 1：写成了减法
    return a - b

def multiply(a, b):
    # Bug 2：未处理非数字输入，会直接崩溃
    return a * b

if __name__ == "__main__":
    print(add(2, 3))       # 预期 5，实际输出 -1
    print(multiply(2, "3")) # 预期报错
