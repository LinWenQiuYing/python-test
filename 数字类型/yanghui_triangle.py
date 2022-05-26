num = int(input("请输入想查看的杨辉三角的层数："))

s = []
for i in range(num):
    item = []
    for j in range(i):
        if j == 0:
            item.append(1)
            print(1, end="\t")
        else:
            item.append(s[i - 1][j - 1] + s[i - 1][j])
            print(s[i - 1][j - 1] + s[i - 1][j], end="\t")
    item.append(1)
    print(1, end="\t")
    print('')
    s.append(item)
# print(s)
