# 文件
import json
from pathlib import Path

data_dir = Path("data") # 输出统一放到 data/，避免污染仓库根目录
data_dir.mkdir(exist_ok=True)

p = data_dir / "demo.txt" # 创建Path对象
p.write_text("第一行\n第二行\n", encoding="utf-8") # 写入文本

with p.open(encoding="utf-8") as f: # 打开文件
    for i, line in enumerate(f, start=1): # 逐行读取文件内容
        print(f"{i}: {line.strip()}") # 去掉换行符并打印

with p.open("a", encoding="utf-8") as f: # 追加模式打开文件
    f.write("第三行\n") # 写入文本
print("-------------------------------")

data = {"name": "capybara", "score": [90, 85]} # 创建字典
json_path = data_dir / "data.json"
json_path.write_text(
    json.dumps(
        data,
        ensure_ascii=False,
        indent=2,
    ),
    encoding="utf-8",
) # 将字典写入json文件
print(json.loads(json_path.read_text(encoding="utf-8"))["score"]) # 读取json文件并打印score键对应的值
print("-------------------------------")

print([f.name for f in Path(".").glob("*.py")]) # 列出当前目录下所有的.py文件
