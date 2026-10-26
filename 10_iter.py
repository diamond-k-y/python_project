# 迭代器与生成器
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print(list(countdown(3)))

it = iter([10, 20])
print(next(it), next(it))

gen = (x * 2 for x in range(5))
print(next(gen), sum(gen))           # 注意：已被消费一个元素

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
