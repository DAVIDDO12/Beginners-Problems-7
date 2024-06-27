numsList = [1,3,8,35,4,2,3]
seen = set()
for num in numsList:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)

