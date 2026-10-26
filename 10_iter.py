# 迭代器与生成器
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print(list(countdown(3)))

it = iter([10, 20])
print(next(it))  # 10
print(next(it))  # 20

gen = (x * 2 for x in range(5))
print(next(gen))  # 0
print(sum(gen))   # 20 注意：0 已被消费，剩下 2+4+6+8

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fib()
print([next(f) for _ in range(8)])

def flatten(*groups):
    for g in groups:
        yield from g

print(list(flatten([1, 2], [3], [])))
