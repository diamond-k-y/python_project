# 流程控制
score = int(input("请输入你的成绩: "))
if score >= 90:
    level = 'A'
elif score >= 75:
    level = 'B'
else:
    level = 'C'
print(f"你的成绩评级为{level}")
print("------------------------------")

total = 0
n = 1
while n <= 100:
    total = total + n # 累加求和 total += n
    n = n + 1
print(f"1到100的和为{total}")
print("------------------------------")

for i in range(1, 6):
    if i == 3:
        print("跳过第3次循环")
        continue # 跳过本次循环，继续下一次循环
    if i == 5:
        print("结束循环")
        break # 结束循环
    print(f"当前循环次数为{i}", end=" ") # end=" " 表示不换行输出
print() # 换行80
print("------------------------------")

print("及格" if score >= 60 else "挂科") # 三元运算符
print("------------------------------")

if (m := 10) > 5: # walrus 运算符
    print(f"m的值为：{m}")
print("------------------------------")

for i in range(2, 10):
    for d in range(2, i):
        if i % d == 0:
            print(f"{i}不是质数")
            break
    else:
        print(f"{i}是质数")
print()
print("------------------------------")