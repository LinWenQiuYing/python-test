# nums = [2, 2, 4, 3, 2, 3, 3, 6, 3, 2, 3, 2]
#
# # 对抗阶段
# major = []
# count = [0]
# for each in nums:
#     if len(major) == 0:
#         major.append(each)
#         count[0] += 1
#         print("0", each, major, count)
#     elif len(major) == 1 and each != major[0]:
#         major.append(each)
#         count.append(1)
#         print("1", each, major, count)
#     elif len(major) == 1 and each == major[0]:
#         count[0] += 1
#         print("2", each, major, count)
#     else:
#         if count[0] == 0 and each != major[1]:
#             major[0] = each
#             count[0] = 1
#             print("3", each, major, count)
#         elif count[1] == 0 and each != major[0]:
#             major[1] = each
#             count[1] = 1
#             print("4", each, major, count)
#         if each == major[0]:
#             count[0] += 1
#             print("5", each, major, count)
#         elif each == major[1]:
#             count[1] += 1
#             print("6", each, major, count)
#         else:
#             count[0] -= 1
#             count[1] -= 1
#             print("7", each, major, count)
#
# # 统计阶段
# if nums.count(major[0]) > len(nums) / 3 and nums.count(major[1]) > len(nums) / 3:
#     print("主要元素是：", major[0], "和", major[1])
# else:
#     print("不存在主要元素。")

nums = [1, 1, 2, 1, 3, 2, 3, 2]

major1 = major2 = nums[0]
count1 = count2 = 0

# 对抗阶段
for each in nums:
    if major1 == each:
        count1 += 1
        continue

    if major2 == each:
        count2 += 1
        continue

    if count1 == 0:
        major1 = each
        count1 = 1
        continue

    if count2 == 0:
        major2 = each
        count2 = 1
        continue

    count1 -= 1
    count2 -= 1
print(major1, major2, count1, count2)
# 统计阶段
if nums.count(major1) > len(nums) / 3:
    print(major1)
if nums.count(major2) > len(nums) / 3:
    print(major2)