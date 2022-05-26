num = int(input("请输入想查看的杨辉三角的层数："))

s = []
for i in range(num):
    item = []
    for j in range(i):
        if j == 0:
            for k in range(num - i - 1):
                print("\t", end="")
            item.append(1)
            print("j", end="")
        else:
            print("\t\t", end="")
            item.append(s[i - 1][j - 1] + s[i - 1][j])
            print(s[i - 1][j - 1] + s[i - 1][j], end="")
    item.append(1)
    if i == 0:
        for k in range(num - i - 1):
            print("\t", end="")
    else:
        print("\t\t", end="")
    print("i", end="")
    print('')
    s.append(item)

