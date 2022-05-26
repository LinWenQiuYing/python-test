# 用列表推导式构建二维数组
s = [[0] * 3 for i in range(3)]
print(s)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 修改二维数组
s[0][1] = 1
print(s)
# [[0, 1, 0], [0, 0, 0], [0, 0, 0]]

# 列表推导式+if
even = [i for i in range(10) if i % 2 == 0]
print(even)
# [0, 2, 4, 6, 8]

words = ['dfas', 'jksad', 'klenwf', 'dfafgq', 'woqn']
dwords = [w for w in words if w[0] == 'd']
print(dwords)
# ['dfas', 'dfafgq']

# 列表推导式+for
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = [col for row in matrix for col in row]
print(flatten)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 列表推到式+for+ifs
nums = [[x, y] for x in range(10) if x % 2 == 0 for y in range(10) if y % 3 == 0]
print(nums)
# [[0, 0], [0, 3], [0, 6], [0, 9], [2, 0], [2, 3], [2, 6], [2, 9], [4, 0], [4, 3], [4, 6], [4, 9], [6, 0], [6, 3],
# [6, 6], [6, 9], [8, 0], [8, 3], [8, 6], [8, 9]]

