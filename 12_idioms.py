# 惯用写法
# 1) 可变默认参数
def bad(item, box=[]):
    box.append(item)
    return box
print(bad(1))                    # [1]
print(bad(2))                    # [1, 2] 上一次的结果被累加！

def good(item, box=None):
    if box is None:          # 不能用 box = box or []，空列表会被当成没传而换掉
        box = []
    box.append(item)
    return box

# 2) == 与 is
a = [1, 2]
b = [1, 2]
print(a == b, a is b)            # is 比身份，小整数/字符串缓存易误判

# 3) 浅拷贝
import copy
m = [[1], [2]]
shallow = m.copy()
deep = copy.deepcopy(m)
shallow[0].append(9)
print(m, deep)

# 4) 边遍历边删
lst = [1, 2, 3, 4]
print([x for x in lst if x % 2 == 0])     # 推荐：新列表
# for x in lst: lst.remove(x)  ← 会漏元素

# 5) 拼接字符串用 join，不要在循环里 += 长字符串
print("".join(str(i) for i in range(100))[:10])

# 6) round 是银行家舍入
print(round(2.5))  # 2 银行家舍入，.5 取偶
print(round(3.5))  # 4
print(round(2.675, 2))  # 2.67 浮点二进制表示导致