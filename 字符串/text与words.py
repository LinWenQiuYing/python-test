# 在word中查找text

text = input("请输入text的内容：")
words = input("请输入words的内容：")

words_list = words.split()
res = []
for item in words_list:
    num = text.find(item)
    while num != -1:
        res.append([num, len(item) - 1 + num])
        num = text.find(item, num + 1)
if len(res) > 0:
    res.sort()
    print(res)
else:
    print("未找到符合要求的word")







