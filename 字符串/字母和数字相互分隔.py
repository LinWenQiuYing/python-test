string = input("请输入：")
num_arr = []
alpha_arr = []
result = []
for s in string:
    if s.isdecimal():
        num_arr.append(s)
    elif s.isalpha():
        alpha_arr.append(s)
if 0 <= len(num_arr) - len(alpha_arr) <= 1:
    result.append(f"{item1, item2}" for item1 in num_arr for item2 in alpha_arr)
print(result)
