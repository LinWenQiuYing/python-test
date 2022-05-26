# 顺时针螺旋顺序输出矩阵中的所有元素
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16],
          [17, 18, 19, 20]]
top = 0
left = 0
bottom = len(matrix)  # 3
right = len(matrix[0])  # 4
result = []
# 第二轮 top: 1, left: 1, bottom: 2, right: 3
while top <= bottom and left <= right:
    # 从左往右遍历
    for i in range(top, right):
        result.append(matrix[top][i])
    # 从上往下遍历
    for j in range(top + 1, bottom):
        result.append(matrix[j][right - 1])
    # 避免重复遍历
    if top + 1 < bottom and left + 1 < right:
        # 从右往左遍历
        for k in range(right - 2, left - 1, -1):
            result.append(matrix[bottom - 1][k])
        # 从下往上遍历
        for l in range(bottom - 2, top, -1):
            result.append(matrix[l][left])
    left += 1
    right -= 1
    top += 1
    bottom -= 1
print(result)