# 列表操作
nums = [3, 1, 4, 1, 5]
nums.append(9) # 在列表末尾添加元素
print(nums) # [3, 1, 4, 1, 5, 9]
print("------------------------------")

nums.insert(0, 2) # 在索引0的位置插入元素2
print(nums) # [2, 3, 1, 4, 1, 5, 9]
print("------------------------------")

nums.remove(1) # 删除列表中第一个出现的元素1
print(nums) # [2, 3, 4, 1, 5, 9]
print("------------------------------")

last = nums.pop() # 删除列表末尾的元素，并返回该元素
print(last) # 9
print("------------------------------")

print(f"元素4在列表中的索引位置: {nums.index(4)}") # 获取元素4在列表中的索引位置
print(f"元素1在列表中出现的次数: {nums.count(1)}") # 统计元素1在列表中出现的次数
print("------------------------------")

nums.sort(reverse=True) # 对列表进行降序排序 reverse=True表示降序排序，默认是升序排序
print(nums) # [5, 4, 3, 2, 1]
print("------------------------------")

print(f"原列表: {nums}")
print(f"排序后的新列表: {sorted(nums)}") # sorted()函数返回一个新的排序后的列表，原列表不变
print("------------------------------")

print(nums + [7]) # [5, 4, 3, 2, 1, 7] 列表的拼接
print([0] * 3) # [0, 0, 0] 列表的重复
print("------------------------------")

matrix = [1, 2, 3], [4, 5, 6], [7, 8, 9] # 二维列表
print(f"二维列表: {matrix}")
print(matrix[1][0]) # 4 第二行第一列
print(matrix[0][:]) # [1, 2, 3] 第一行的全部元素
print("------------------------------")

print([x * x for x in range(6) if x % 2 == 0]) # 列表推导式，生成0到5的平方数
print("------------------------------")

grid = [[r * c for c in range(3)] for r in range(2)] # 二维列表推导式，生成3x2的乘法表
print(f"二维列表推导式: {grid}")
print("------------------------------")

first, *mid, last = "abcde" # 列表解包，*mid表示中间的元素
print(f"first: {first}, mid: {mid}, last: {last}") # first: a, mid: ['b', 'c', 'd'], last: e
print("------------------------------")

t = (1, 2, 3) # 元组，类似于列表，但不可变
print(f"元组: {t}")
one, two, three = t # 元组解包
print(f"one: {one}, two: {two}, three: {three}") # one: 1, two: 2, three: 3
print("------------------------------")

print(f"元组的长度: {len(t)}") # 获取元组的长度
print(f"元组的第一个元素: {t[0]}") # 获取元组的第一个元素
print(f"元组拼接后: {t + (4,)}") # 元组拼接
print(f"元组重复后: {t * 2}") # 元组重复
print("------------------------------")

bad = [[]] * 3 # 创建一个包含三个空列表的列表
bad[0].append(1) # 向第一个空列表中添加元素1
good = [[] for _ in range(3)] # 创建一个包含三个独立空列表的列表
good[0].append(1) # 向第一个独立空列表中添加元素1
print(f"bad: {bad}, good: {good}") # bad: [[1], [1], [1]], good: [[1], [], []]