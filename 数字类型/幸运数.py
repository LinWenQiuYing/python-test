s = [[10, 36, 52],
     [33, 24, 88],
     [66, 76, 99],
     [77, 82, 95]]
# rowLen = len(s[0])
# colLen = len(s)
# 行列数应该按照下面的取法，与我的想法正好相反，仔细想想我的相法是错误的
rowNum = len(s)
colNum = len(s[0])
print('len', rowNum, colNum)

min_row = [1024] * rowNum
max_col = [0] * colNum

# # 遍历找到每行的最小值
# for i in range(rowNum):
#     min_row[i] = min(s[i])
# print(min_row)
#
# # 遍历找到每列的最大值
# for i in range(colNum):
#     for j in range(rowNum):
#         print(s[j][i])
#         max_col[i] = max(max_col[i], s[j][i])
# print(max_col)

for i in range(rowNum):
    for j in range(colNum):
        print('index', i, j, s[i][j], min_row[i], max_col[j])
        min_row[i] = min(s[i][j], min_row[i])
        max_col[j] = max(s[i][j], max_col[j])
        print(min_row, max_col)
print(min_row, max_col)

for i in range(rowNum):
    for j in range(colNum):
        if min_row[i] == max_col[j]:
            print(i, j)
            break
