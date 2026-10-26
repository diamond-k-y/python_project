# 内置函数与常用标准库
import itertools, math, random, re
from collections import Counter, defaultdict, deque, namedtuple
from datetime import datetime, date, timedelta

names, scores = ["a", "b"], [90, 80]
print(list(zip(names, scores)))
print([f"{i}:{n}" for i, n in enumerate(names, 1)])
print(list(map(str.upper, names)), list(filter(None, [0, 1, "", "x"])))
print(any(scores), all(s > 60 for s in scores), max(scores), sum(scores))
print(min(names, key=len))

print(math.sqrt(16), math.floor(2.7), round(2.675, 2))
print(random.randint(1, 10), random.choice(names), random.sample(names, 1))

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"), date.today() + timedelta(days=7))

print(re.findall(r"\d+", "a1b22c333"))
print(re.sub(r"\s+", " ", "a   b \t c").strip())

print(list(itertools.chain([1, 2], [3])))
print(list(itertools.product("ab", [1, 2])))
print(list(itertools.islice(itertools.count(10), 3)))

dd = defaultdict(list)
for k, v in [("a", 1), ("a", 2)]:
    dd[k].append(v)
print(dict(dd), deque([1, 2, 3]).popleft())
Point = namedtuple("Point", "x y")
print(Point(1, 2).x)
