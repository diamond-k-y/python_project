# 文件
import json
from pathlib import Path

p = Path("demo.txt") # 创建Path对象
p.write_text("第一行\n第二行\n", encoding="utf-8") # 写入文本

with p.open(encoding="utf-8") as f: # 打开文件
    for i, line in enumerate(f, start=1): # 逐行读取文件内容
        print(f"{i}: {line.strip()}") # 去掉换行符并打印

with p.open("a", encoding="utf-8") as f: # 打开文件
    f.write("第三行\n") # 写入文本
print("-------------------------------")

data = {"name": "capybara", "score": [90, 85]} # 创建字典
Path("data.json").write_text(
    json.dumps(
        data,
        ensure_ascii=False,
        indent=2,
    ),
    encoding="utf-8",
) # 将字典写入json文件
print(json.loads(Path("data.json").read_text(encoding="utf-8"))["score"]) # 读取json文件并打印score键对应的值
print("-------------------------------")

print([f.name for f in Path(".").glob("*.py")]) # 列出当前目录下所有的.py文件