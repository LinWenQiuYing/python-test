# 凯撒密码是一种通过位移加密的方法，对 26 个（大小写）字母进行位移加密
print(chr(91), chr(92), chr(93), chr(94), chr(95), chr(96))
# [ \ ] ^ _ `
print(ord("a"), ord("z"))
# 97 122
print(ord("A"), ord("Z"))
# 65 90

password = input("请输入需要加密的明文（只支持英文字母）：")
step = int(input("请输入移动的位数："))

result = []
x = 0
for s in password:
    if 97 <= ord(s) <= 122:
        # a ~ z
        x = (ord(s) - ord("a") + step) % 26 + ord("a")
        result.append(chr(x))
    elif 65 <= ord(s) <= 90:
        # A ~ Z
        x = (ord(s) - ord("A") + step) % 26 + ord("A")
        result.append(chr(x))
    else:
        result.append(s)

print("".join(result))

