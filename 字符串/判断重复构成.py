text = input("请输入一个由字母构成的字符串：")
if text.isalpha():
    n = len(text)
    flag = False  # 作为判断是否符合要求的标志变量
    for i in range(1, n // 2 + 1):
        word = text[0: i]
        if n % i == 0:
            start = i
            while text.startswith(word, start):
                start += len(word)
                if start == n:
                    flag = True
                    break
    print("flag", flag)
else:
    print("请输入一个由字母构成的字符串!")
