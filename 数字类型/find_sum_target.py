# 在10000个随机数里找到两个数的和为输入的目标数字，并输出两个数的位置
import random
list1 = []
result = []
target = ""

for i in range(10000):
    x = random.randint(1, 65535)
    list1.append(x)

print(list1)
print(len(list1))

target = int(input("请录入目标整数："))

for i in list1:
    for j in list1[i:]:
        if i + j == target:
            result.append([list1.index(i), list1.index(j)])
            break
if len(result):
    for item in result:
        print(item)
else:
    print("找不到符合要求的两个数字")
