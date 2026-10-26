# 字符串与格式化
str = "hello, capyBara"
print(str[0]) # h 获取字符串的第一个字符
print(str[-1]) # a 获取字符串的最后一个字符
print(str[1:4]) # ell 获取字符串的子串
print(str[7:10]) # cap 获取字符串的子串
print(str[::-1]) # arabyapc 获取字符串的反转
print(len(str)) # 8 获取字符串的长度
print(str.upper()) # CAPYBARA 转换为大写
print(str.lower()) # capybara 转换为小写
print(str.capitalize()) # Hello, capybara 首字母大写
print(str.title()) # Hello, Capybara 每个单词首字母大写
print("打个招呼吧：{}".format(str)) # format 格式化输出
print(f"打个招呼吧：{str}") # f-string 格式化输出