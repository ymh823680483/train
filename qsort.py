def qsort(numlist):
    if len(numlist) < 2:
        return numlist
    else:
        front=[]
        back =[]
        for i in numlist:
            if i>numlist[0]:
                front.append(i)
            if i<numlist[0]:
                back.append(i)
        res = qsort(front) +[numlist[0]] +qsort(back)
        return res
numlist = [44,5,1,7,15,4,66,134,65,4,6,3,5,90,78,45]
res = qsort(numlist)
print(res)
