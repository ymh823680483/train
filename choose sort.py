def choose_sort(numlist):
    reslist = []
    while len(numlist) > 0:
        reslist.append(find_max(numlist))
        numlist.remove(find_max(numlist))
    return reslist


def find_max(numlist):
    test = 0
    for i in numlist:
        if test < i:
            test = i
    maxnum = test
    return maxnum


numlist = [44, 5, 1, 7, 15, 4, 66, 134, 165, 4, 6, 3, 5, 90, 78, 45]
res = choose_sort(numlist)
print(res)
