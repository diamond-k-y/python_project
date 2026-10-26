# 变量、类型、运算
name = "capybara" # 字符串类型
age = 18 # 整数类型
height = 1.68 # 浮点数类型
ok = False # 布尔类型

print(type(name)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(height)) # <class 'float'>
print(type(ok)) # <class 'bool'>

a, b = 10, 20 # 多变量赋值
a, b = b, a # 交换变量值
x = y = z = 100 # 链式赋值
print(a, b) # 20 10 交换后的结果
print(x, y, z) # 100 100 100 链式赋值

print(7 / 2) # 3.5 浮点数除法
print(7 // 2) # 3 整数除法
print(7 % 2) # 1 取余运算
print(2 ** 3) # 8 幂运算
print(0.1 + 0.2) # 0.30000000000000004 浮点数精度问题
print(round(0.1 + 0.2, 2)) # 0.3 四舍五入

print(int("123")) # 123 字符串转整数
print(float("3.14")) # 3.14 字符串转浮点数
print(str(456)) # '456' 整数转字符串
print(bool("123")) # True 字符串转布尔
print(bool("")) # False 字符串转布尔
n = int(input("请输入一个整数：")) # 输入一个整数并转换为整数类型
print(n * 2) # 输出输入整数的两倍