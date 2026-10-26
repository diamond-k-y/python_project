# 字典
person = {"name": "capybara", "age": 18, "gender": "female"} # 字典是无序的键值对集合，使用{}表示
person["city"] = "china" # 添加键值对
print(f"name对应的值: {person['name']}") # capybara 获取键对应的值
print(f"job对应的值: {person.get('job')}") # None 获取键对应的值，如果键不存在则返回None
print(f"job对应的值: {person.get('job', '未知')}") # 未知 获取键对应的值，如果键不存在则返回默认值
for k, v in person.items(): # 遍历字典的键值对
    print(f"{k}: {v}")
print("------------------------------")

print(f"字典的长度: {len(person)}") # 获取字典的长度
print(f"字典的所有键: {person.keys()}") # 获取字典的所有键
print(f"字典的所有值: {person.values()}") # 获取字典的所有值
print(f"字典的所有键值对: {person.items()}") # 获取字典的所有键值对
print("------------------------------")

print(person.pop("city")) # china 删除字典中指定键的键值对，并返回该键对应的值
print("name" in person) # True 判断字典中是否存在指定的键
print(list(person.keys())) # ['name', 'age', 'gender'] 将字典的键转换为列表
print({"a": 1} | {"b": 2}) # {'a': 1, 'b': 2} 字典的合并，Python 3.9+ 支持
print("------------------------------")

counts = {}
for w in "a b a c b a".split(): # 统计每个单词出现的次数
    counts[w] = counts.get(w, 0) + 1 # 如果键不存在则返回0，否则返回键对应的值
print(counts) # {'a': 3, 'b': 2, 'c': 1} 打印统计结果
print("------------------------------")

from collections import Counter # 导入Counter类
print(Counter("a b a c b a".split()).most_common(2)) # [('a', 3), ('b', 2)] 获取出现次数最多的前2个元素
print("------------------------------")

s1, s2 = {1, 2, 3}, {3, 4} # 集合，类似于字典，但只有键没有值，使用{}表示
print(s1 | s2, s1 & s2, s1 - s2, s1 ^ s2) # {1, 2, 3, 4} {3} {1, 2} {1, 2, 4} 集合的并集、交集、差集和对称差集
print({x % 3 for x in range(10)}) # {0, 1, 2} 集合推导式，生成0到9的数对3取余的结果