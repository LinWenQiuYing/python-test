# v1 = input("请输入第一个版本号，v1 = ")
# v2 = input("请输入第一个版本号，v2 = ")
# length1 = len(v1)
# length2 = len(v2)
# v1_flag = False
# v2_flag = False
# length = min(length1, length2)
# for i in range(length):
#     if v1[i] != "." and v2[i] != ".":
#         if int(v1[i]) > int(v2[i]):
#             v1_flag = True
#             break
#         elif int(v1[i]) < int(v2[i]):
#             v2_flag = True
#             break
#     elif v1[i] != "." and v2[i] == ".":
#         v1_flag = True
#         break
#     elif v1[i] == "." and v2[i] != ".":
#         v2_flag = True
#         break
# if v1_flag:
#     print("v1")
# elif v2_flag:
#     print("v2")
# else:
#     flag = False
#     if length1 > length2:
#         for i in range(length, length1):
#             if v1[i] != "." and v1[i] != "0":
#                 # 遍历版本号，判断是否有x.0.0.0的情况，此情况等价于x
#                 # flag为True，表示不全为0
#                 flag = True
#                 break
#         if flag:
#             print("v1")
#         else:
#             print("版本号相同")
#     elif length1 < length2:
#         for i in range(length, length2):
#             if v2[i] != "." and v2[i] != "0":
#                 # 遍历版本号，判断是否有x.0.0.0的情况，此情况等价于x
#                 # flag为True，表示不全为0
#                 flag = True
#                 break
#         if flag:
#             print("v2")
#         else:
#             print("版本号相同")
#     else:
#         print("版本号相同")
#
v1 = input("请输入第一个版本号，v1 = ")
v2 = input("请输入第二个版本号，v2 = ")

n, m = len(v1), len(v2)
i, j = 0, 0
x, y = 0, 0

while i < n or j < m:
    x = 0
    while i < n and v1[i] != '.':
        x = x * 10 + int(v1[i])
        i += 1
        print("x", x)
    i += 1

    y = 0
    while j < m and v2[j] != '.':
        y = y * 10 + int(v2[j])
        j += 1
        print("y", y)
    j += 1

    if x > y:
        print("v1")
        break
    elif x < y:
        print("v2")
        break
print("x, y", x, y)
if x == y:
    print("v1 = v2")
