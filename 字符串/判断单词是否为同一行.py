# 给定一个字符串数组 words，只返回可以使用在美式键盘同一行的字母打印出来的单词
words = input("请输入单词组，用“,”隔开：").split(",")
line1 = "qwertyuiop"
line2 = "asdfghjkl"
line3 = "zxcvbnm"

result = []
for word in words:
    num1 = 0
    num2 = 0
    num3 = 0
    text = word.lower()
    length = len(word)
    for s in text:
        if line1.find(s) > -1:
            num1 += 1
        elif line2.find(s) > -1:
            num2 += 1
        elif line3.find(s) > -1:
            num3 += 1
    if num1 == length or num2 == length or num3 == length:
        result.append(word)
print(",".join(result))
