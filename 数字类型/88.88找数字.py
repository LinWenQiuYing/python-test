# 在88*88的二维数组中找到指定整数
import random

s = []
for i in range(88):
    s.append([])
    for j in range(88):
        s[i].append(random.randint(0, 1024))
# s = [[0] * 88 for i in range(88)]
# for i in range(88):
#     for j in range(88):
#         s[i][j] = random.randint(0, 1024)
print(s)

temp = int(input("请输入一个待匹配的整数："))
for i in range(88):
    for j in range(88):
        if s[i][j] == temp:
            print(i, j)
