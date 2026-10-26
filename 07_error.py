# 异常处理
def to_int(text):
    try:
        return int(text)
    except ValueError as e:
        print(f"不是整数：{e}")
        return None
    else:
        print("成功分支")
    finally:
        print("总会执行")
print(to_int("123")) # 123
print(to_int("abc")) # None
print("------------------------------")

class AgeError(ValueError): # 自定义异常类，继承自ValueError
    pass
def check_age(age):
    if age < 0:
        raise AgeError("年龄不能为负数") # 抛出自定义异常
    return age
try:
    print(check_age(-1))
    check_age(-1)
except AgeError as e:
    print(f"捕获到自定义异常：{e}")
try:
    1 /0
except ZeroDivisionError as e:
    print(f"捕获到零除异常：{e}")