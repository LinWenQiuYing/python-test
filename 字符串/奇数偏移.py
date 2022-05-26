s = input("请按规则输入一个字符串：")

length = len(s)
res = []
# 获取字母 a 的编码值
base = ord('a')

# 从第一个元素开始，每次迭代跳过一个元素
for i in range(0, length, 2):
    # ord(s[i]) - base 操作得到一个字母的偏移值，比如 b 就是 1
    # 跟 26 求余数的作用是防止溢出，循环计算偏移
    shift = chr((ord(s[i]) - base + ord(s[i + 1])) % 26 + base)
    print(s[i] + shift, end="")