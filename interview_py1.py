# 去重，以元素出现次数，降序排序
def solution(xlist):
    x_set = set(xlist)
    x_dict = {}

    for i in x_set :
        x_dict[i]=xlist.count(i)

    x = sorted(x_dict.items(), key = lambda x : x[1], reverse = True)
    print('x = ', x)
    y = [i[0] for i in x]

    return y


#生成测试数据
import random
j = 0
zz = []

while j < 5:
    x = list(range(10))
    y = list(range(10))
    random.shuffle(x)
    random.shuffle(y)
    z = []

    i = 0
    while i < 10:
        num = x.pop()
        count = y.pop()
        for _ in range(count):
            z.append(num)
        i = i + 1

    random.shuffle(z)
    print('z = ', z)
    zz.append(z)
    j = j + 1


#测试solution
print()
for x in zz:
    print(solution(x))

