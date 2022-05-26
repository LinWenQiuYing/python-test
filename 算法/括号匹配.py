target = input("请输入检测字符串：")

list1 = []
flag = True

for item in target:
    if item == "(" or item == "（" or item == "[" or item == "【" or item == "{":
        list1.extend(item)
    elif item == ")":
        if len(list1) and list1[-1] == "(":
            list1 = list1[:len(list1)-1]
        else:
            flag = False
            break
    elif item == "}":
        if len(list1) and list1[-1] == "{":
            list1 = list1[:len(list1)-1]
        else:
            flag = False
            break
    elif item == "]":
        if len(list1) and list1[-1] == "[":
            list1 = list1[:len(list1)-1]
        else:
            flag = False
            break
    elif item == "】":
        if len(list1) and list1[-1] == "【":
            list1 = list1[:len(list1)-1]
        else:
            flag = False
            break
    elif item == "）":
        if len(list1) and list1[-1] == "（":
            list1 = list1[:len(list1)-1]
        else:
            flag = False
            break
if flag:
    print("合法^o^")
else:
    print("非法T_T")
