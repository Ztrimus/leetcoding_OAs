# incorrect solution fails in Test cases
def finMin(boxes):
    box = sorted(boxes)
    dif = float("inf")
    count = 0
    while 1:
        l, r = 0, len(box)-1
        if (box[r] - box[l]) == 0 or (box[r] - box[l]) == 1:
            return count
        while l<len(box)-1 and box[l] == box[l+1]:
            l+=1
        box[l]+=1
        while r>l and box[r] == box[r-1]:
            r-=1
        box[r]-=1
        if dif == box[r] - box[l] or dif < box[r]-box[l]:
            return count
        dif = box[r] - box[l]
        count+=1

print(finMin([2,4,1]))

print(finMin([4,4,4,4,4]))

print(finMin([5,5,8,7]))

print(finMin([6,5,4,1]))
