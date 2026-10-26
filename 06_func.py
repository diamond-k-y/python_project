# 函数
def greet(name, greeting="您好", *, punct="!"): # 定义函数，带有默认参数和关键字参数
    return f"{greeting}, {name}{punct}" # 返回格式化的字符串

print(greet("Alice")) # 您好, Alice!
print(greet("Bob", greeting="Hello")) # Hello, Bob!
print(greet("Charlie", punct=".")) # 您好, Charlie.
print("-------------------------------")

def stats(*args, **kwargs): # 定义函数，带有可变参数和关键字参数
    return sum(args), kwargs # 返回可变参数的和和关键字参数的字典
print(stats(1, 2, 3))
print(stats(1, 2, mode="avg"))
print("-------------------------------")

def outer(x): # 定义外部函数
    def inner(y): # 定义内部函数
        return x + y # 内部函数访问外部函数的变量 闭包
    return inner # 返回内部函数
print(outer(5)(3)) # 8
print("-------------------------------")

def make_counter():
    c = 0
    def bump():
        nonlocal c # nonlocal关键字用于在内部函数中修改外部函数的变量
        c += 1
        return c
    return bump
cnt = make_counter()
print(cnt(), cnt(), cnt()) # 1 2 3
print("-------------------------------")

print(sorted([(2, "b"), (1, "a")], key=lambda p: p[0])) # [(1, 'a'), (2, 'b')] 使用lambda函数作为排序的key
print(sorted(["bb", "a", "ccc"], key=len, reverse=True)) # ['ccc', 'bb', 'a'] 使用lambda函数作为排序的key，并指定降序排序
print("-------------------------------")

def mean(nums:list[float]) -> float: # 定义函数，带有类型注解
    return sum(nums) / len(nums) # 返回列表的平均值
print(mean([1, 2, 3, 4, 5])) # 3.0