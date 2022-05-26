import timeit
test1 = timeit.repeat("x = [1, 2, 3]", number=10000, repeat=100)
test2 = timeit.repeat("y=(1, 2, 3)", number=10000, repeat=100)
print(test1)
print(test2)
time1 = 0
time2 = 0
for i in test1:
    time1 += i
time1 = time1 / 10

for j in test2:
    time2 += j
time2 = time2 / 10
print(time1, time2)
if time1 > time2:
    print("创建元组更快")
elif time1 < time2:
    print("创建列表更快")
else:
    print("一样快")
