numsList = [1,3,8,35,4,2,3]
seen = set()
for num in numsList:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)

String = input("Enter a phrase:")
Words = set(String.split())
A = sum(word.count("a")for word in Words)
print(A)

list1 = input("Enter numbers for the first list, separated by spaces: ").split()
list2 = input("Enter numbers for the second list, separated by spaces: ").split()
list1 = [int(num) for num in list1]
list2 = [int(num) for num in list2]
commonnumbers = set(list1) & set(list2)
commonnumbers = list(commonnumbers)
for integer in range(len(commonnumbers)):
    for number in range(integer+1,len(commonnumbers)):
        if commonnumbers[integer]>commonnumbers[number]:
            commonnumbers[integer],commonnumbers[number] = commonnumbers[number],commonnumbers[integer]
print(commonnumbers)
