# 字符串与格式化
s = "hello, capyBara"
print(s[0]) # h 获取字符串的第一个字符
print(s[-1]) # a 获取字符串的最后一个字符
print(s[1:4]) # ell 获取字符串的子串
print(s[7:10]) # cap 获取字符串的子串
print(s[::-1]) # araBypac ,olleh 获取字符串的反转
print(len(s)) # 15 获取字符串的长度
print(s.upper()) # HELLO, CAPYBARA 转换为大写
print(s.lower()) # hello, capybara 转换为小写
print(s.capitalize()) # Hello, capybara 首字母大写
print(s.title()) # Hello, Capybara 每个单词首字母大写
print("打个招呼吧：{}".format(s)) # 打个招呼吧：hello, capyBara format 格式化输出
print(f"打个招呼吧：{s}") # 打个招呼吧：hello, capyBara f-string 格式化输出
