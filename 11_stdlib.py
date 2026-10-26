# 内置函数与常用标准库
import itertools, math, random, re
from collections import Counter, defaultdict, deque, namedtuple
from datetime import datetime, date, timedelta

names, scores = ["a", "b"], [90, 80]
print(list(zip(names, scores)))
print([f"{i}:{n}" for i, n in enumerate(names, 1)])
print(list(map(str.upper, names)))  # ['A', 'B']
print(list(filter(None, [0, 1, "", "x"])))  # [1, 'x'] 过滤掉假值
print(any(scores))  # True
print(all(s > 60 for s in scores))  # True
print(max(scores))  # 90
print(sum(scores))  # 170
print(min(names, key=len))

print(math.sqrt(16))  # 4.0
print(math.floor(2.7))  # 2
print(round(2.675, 2))  # 2.67 浮点二进制表示导致，不是 2.68
print(random.randint(1, 10))  # 1~10 的随机整数
print(random.choice(names))  # 随机取一个元素
print(random.sample(names, 1))  # 随机取 1 个，返回列表

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))  # 按格式输出当前时间
print(date.today() + timedelta(days=7))  # 一周后的日期

print(re.findall(r"\d+", "a1b22c333"))
print(re.sub(r"\s+", " ", "a   b \t c").strip())

print(list(itertools.chain([1, 2], [3])))
print(list(itertools.product("ab", [1, 2])))
print(list(itertools.islice(itertools.count(10), 3)))

dd = defaultdict(list)
for k, v in [("a", 1), ("a", 2)]:
    dd[k].append(v)
print(dict(dd))  # {'a': [1, 2]} 默认值自动创建列表
print(deque([1, 2, 3]).popleft())  # 1 从左侧弹出
Point = namedtuple("Point", "x y")
print(Point(1, 2).x)
