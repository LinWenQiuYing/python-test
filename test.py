from typing import Tuple
import keyword

result = 0
for each in range(-10, -100, -20):
    result += each
print(result)

print(ord('是'))

x = []
print(x)

print([1, 2, 3, 4, 5][:3])

print([1, 2, 3, 4, 5][::2])

print([5, "上", 4, "山", 3, "打", 2, "老", 1, "虎"][-2::-2])

list1 = [1, 2, 8, 9]
list2 = [3, 4, 5, 6, 7]
list3 = list1[:2] + list2 + list1[2:]
print('list3', list3)

s = [1, 2, 3, 4, 5]
s.insert(5, 6)
print(s)
s.extend(["FishC"])
print(s)

s = [1, 2, 3, 4, 5]
s[5:5] = ["上山打老虎"]
print(s)
# [1, 2, 3, 4, 5, '上山打老虎']

s = [1, 2, 3, 4, 5]
s[5:5] = "上山打老虎"
print(s)
# [1, 2, 3, 4, 5, '上', '山', '打', '老', '虎']

s = [1, 2, 3, 4, 5]
s[len(s) - 2:] = [2, 1, 0]
print(s)
# [1, 2, 3, 2, 1, 0]

heros = ['蜘蛛侠', '绿巨人', '黑寡妇', '鹰眼', '灭霸', '雷神']
heros[2:3] = ["神奇女侠"]
print(heros)
# ['蜘蛛侠', '绿巨人', '神奇女侠', '鹰眼', '灭霸', '雷神']

heros[0:2] = ["猪猪侠", "女巨人"]
print(heros)
# ['猪猪侠', '女巨人', '神奇女侠', '鹰眼', '灭霸', '雷神']

s = [1, 2, 3, 4, 5]
s[:] = "FishC"
print(s)
# ['F', 'i', 's', 'h', 'C']

s = [1, 2, 3, 4, 5]
s[2:4] = []
print(s)
# [1, 2, 5]

s = [1, 2, 3, 4, 5]
t = s
s[2] = 1
print(t)
# [1, 2, 1, 4, 5]

a = '小甲鱼'
b = '小甲鱼'
print(id(a))
print(id(b))
print(a is b)

c = [[1, 2, 3], [4, 5, 6]] + [7, 8, 9]
print(c)
# [[1, 2, 3], [4, 5, 6], 7, 8, 9]

# 三维列表
z = [0] * 3
print(z)
for i in range(3):
    z[i] = [0] * 2
    for j in range(2):
        z[i][j] = [0] * 2
print(z)

x = 1
y = x
x = 2
print(y)

x = [1, 2, 3]
y = x
y[1] = 1
print(x == y, x, y)
# True [1, 1, 3] [1, 1, 3]
# 不可思议，这就是浅拷贝吧

x = [[1, 2, 3], [4, 5, 6]]
y = x.copy()
y.append(7)
y[1].append(8)
print(x, y)
# x:[[1, 2, 3], [4, 5, 6, 8]] y:[[1, 2, 3], [4, 5, 6, 8], 7]
# 因为是浅拷贝，当处理一维列表时，x与y有区别，当处理更高维度时，x与y有着相同的引用，便得到了相同的结果

s = [(i + 1) * (i + 1) for i in range(6)]
print(s)

matrix = [[i, i + 2] for i in range(6)]
print(matrix)

double = []
for c in 'Fishc':
    double.append(c * 2)
print(double)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
diag = [i * matrix[i][i] for i in range(len(matrix))]
print(diag)

x = 'Fishc'
y = [x for x in '123']
print(x, y)
# Fishc ['1', '2', '3']

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
s = [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]
print(s)

s = [[8] * 5 for i in range(4)]
s[1][1] = 1
print(s)
# [[8, 8, 8, 8, 8], [8, 1, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8]]

result = [i / 2 for i in range(10) if i % 2 == 0]
print(result)
# [0.0, 1.0, 2.0, 3.0, 4.0]

result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i / 2)
print(result)
# [0.0, 1.0, 2.0, 3.0, 4.0]

result = [[x, y] for x in range(10) if x % 2 == 0 for y in range(10) if y % 2 != 0]
print(result)
# [[0, 1], [0, 3], [0, 5], [0, 7], [0, 9], [2, 1], [2, 3], [2, 5], [2, 7], [2, 9], [4, 1], [4, 3], [4, 5], [4, 7],
# [4, 9], [6, 1], [6, 3], [6, 5], [6, 7], [6, 9], [8, 1], [8, 3], [8, 5], [8, 7], [8, 9]]

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
length = len(matrix)
# result = [matrix[length - 1 - x][len(matrix[x]) - 1 - y] for x in range(length) for y in range(len(matrix[x]))]
# [col for row in matrix for col in row]--正序输出 + [::-1]取反
result = [col for row in matrix for col in row][::-1]
print(result)
# [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

colors = ["BLACK", "WHITE"]
sizes = ["WS", "WM", "WL", "S", "M", "L", "XL", "2XL", "3XL", "4XL"]

result = [[x, y] for x in colors for y in sizes]
print(result)

# 转置矩阵
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
# Tmatrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
Tmatrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(Tmatrix)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]] 神奇！
# 神奇！用for循环还原
Tmatrix = []
# for j in range(len(matrix[0])):
#     item = []
#     for i in range(len(matrix)):
#         item.append(matrix[i][j])
#     Tmatrix.append(item)
for i in range(len(matrix[0])):
    Tmatrix.append([row[i] for row in matrix])
print(Tmatrix)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 字符串
x = "12321"
print("是回文数" if x == x[::-1] else "不是回文数")

x = "I love FishC"
print(x.capitalize())
# I love fishc
print(x.casefold())
# i love fishc
print(x.title())
# I Love Fishc
print(x.swapcase())
# i LOVE fISHc
print(x.upper())
# I LOVE FISHC
print(x.lower())
# i love fishc

x = "有内鬼，停止交易！"
print(x.center(15))
# '   有内鬼，停止交易！   '
print(x.ljust(15))
# '有内鬼，停止交易！      '
print(x.rjust(15))
# '      有内鬼，停止交易！'
print(x.zfill(15))
# '000000有内鬼，停止交易！'
print("520".zfill(5))
# '00520'
print("-520".zfill(5))
# -0520
print(x.center(15, "淦"))
# '淦淦淦有内鬼，停止交易！淦淦淦'
print(x.ljust(15, "淦"))
# '有内鬼，停止交易！淦淦淦淦淦淦'
print(x.rjust(15, "淦"))
# '淦淦淦淦淦淦有内鬼，停止交易！'

print("-520".zfill(10))
# '-000000520'
print("-520".rjust(10, "0"))
# '000000-520'

print("-520".center(6, "0").zfill(10))
# '00000-5200'

print("I love FishC".swapcase()[::-1])
# 'cHSIf EVOL i'

arr = ["123", "33211", "12321", "13531", "112233"]
result = [item for item in arr if item == item[::-1]]
print(result)
# ['12321', '13531']

str1 = "xxxxx"
print(str1.count("xx"))
# 2 因为count方法返回在字符串中 不重叠 的出现次数

x = "上海自来水来自海上"
print(x.rindex("来水来"))
# 3

print("I love FishC.com".translate(str.maketrans("ABCDEFG", "1234567")))
# I love 6ish3.com

print("I love FishC.com".translate(str.maketrans("love", "1234", "love")))
# I  FishC.cm

x = "我爱Python"
# startswith(prefix[, start[, end]]) 方法用于判断 prefix 参数指定的子字符串是否出现在字符串的起始位置：
print(x.startswith("我爱"))
# True
print(x.startswith("爱", 1))
# True
print(x.startswith("x"))
# False

# endswith(suffix[, start[, end]]) 方法则相反，用于判断 suffix 参数指定的子字符串是否出现在字符串的结束位置：
print(x.endswith("Python"))
# True
print(x.endswith("Python", 3))
# False
print(x.endswith("Py", 0, 4))
# True

# 这个 prefix 和 suffix 参数呀，其实是支持以元组的形式传入多个待匹配的字符串的：
x = "她爱Python"
if x.startswith(("你", "我", "她")):
    print("总有人喜爱Python")

# 如果你希望判断一个字符串中的所有单词是否都是以大写字母开头，其余字母均为小写，那么可以使用 istitle() 方法进行测试：
x = "I Love Python"
print(x.istitle())
# True

# 如果你希望判断一个字符串中所有字母是否都是大写，可以使用 isupper() 方法进行测试：
print(x.isupper())
# False
print(x.upper().isupper())
# True

print("\n".isprintable())
# False
print(r"\n".isprintable())
# True
print("a", "I love FishC\s".isprintable())
# \s 不是转义字符

# isdecimal()、isdigit() 和 isnumeric() 三个方法都是用来判断数字的。
# 首先是十进制数字：
x = "12345"
print(x.isdecimal())
# True
print(x.isdigit())
# True
print(x.isnumeric())
# True

# 如果写成罗马数字：
x = "ⅠⅡⅢⅣⅤ"
print(x.isdecimal())
# False
print(x.isdigit())
# False
print(x.isnumeric())
# True

# 或者中文数字:
x = "一二三四五"
print(x.isdecimal())
# False
print(x.isdigit())
# False
print(x.isnumeric())
# True

# 繁体中文数字：
x = "壹贰叁肆伍"
print(x.isdecimal())
# False
print(x.isdigit())
# False
print(x.isnumeric())
# True

# isalnum() 方法则是集大成者，只要 isalpha()、isdecimal()、isdigit() 或者 isnumeric() 任意一个方法返回 True，结果都为 True。
# isalpha() 方法判断的字母是 Unicode 编码中定义的字母，也就是说包括中文，isascii()判断它是否为 ASCII 编码
# isidentifier() 方法用于判断该字符串是否一个合法的 Python 标识符
# 由于对 Unicode 编码的支持，Python 是可以使用中文作为合法标识符的。
print("I a good gay".isidentifier())
# False
print("I_a_good_gay".isidentifier())
# True
print("520FishC".isidentifier())
# False

# 如果你想判断一个字符串是否为 Python 的保留标识符，就是像 “if”、“for”、“while” 这些关键字的话，可以使用 keyword 模块的 iskeyword() 函数来实现：
# 得先引入keyword
keyword.iskeyword("str")
# True
keyword.iskeyword("py")
# False

print("www.ilovefishc.com".lstrip("wcom."))
# ilovefishc.com
print("www.ilovefishc.com".rstrip("wcom."))
# www.ilovefish
print("www.ilovefishc.com".strip("wcom."))
# ilovefish

print("www.ilovefishc.com".removeprefix("w."))
# www.ilovefishc.com
print("www.ilovefishc.com".removeprefix("www."))
# ilovefishc.com

print("苟日新，日日新，又日新".split("，"))
# ['苟日新', '日日新', '又日新']
print("苟日新，日日新，又日新".split("，", 0))
# ['苟日新，日日新，又日新']
print("苟日新，日日新，又日新".split("，", 1))
# ['苟日新', '日日新，又日新']
print("苟日新，日日新，又日新".split("，", 2))
# ['苟日新', '日日新', '又日新']
print("https://ilovefishc.com/html5/index.html".split("/"))
# ['https:', '', 'ilovefishc.com', 'html5', 'index.html']

s = " ".join(("I", "love", "fishc"))
print(s)

print(",\n".join("FishC"))
# F,
# i,
# s,
# h,
# C

print(ord("a"), ord("z"))
# 97
print(ord("A"), ord("Z"))
# 65



