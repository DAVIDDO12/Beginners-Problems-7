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

list1 = input("Enter numbers for the first list(separated by spaces): ").split()
list2 = input("Enter numbers for the second list(separated by spaces): ").split()
list1 = [int(num) for num in list1]
list2 = [int(num) for num in list2]
commonnumbers = set(list1) & set(list2)
commonnumbers = list(commonnumbers)
for integer in range(len(commonnumbers)):
    for number in range(integer+1,len(commonnumbers)):
        if commonnumbers[integer]>commonnumbers[number]:
            commonnumbers[integer],commonnumbers[number] = commonnumbers[number],commonnumbers[integer]
print(commonnumbers)

People = int(input("Enter the number of people: "))
Alllanguages = []
Commonlanguages = []
for i in range(People):
    Numberoflanguages = int(input("Enter the number of languages for person " + str(i + 1) + ": "))
    Languages = input("Enter the languages spoken by person " + str(i + 1) + " (separated by spaces): ").split()
    for language in Languages:
        if language not in Alllanguages:
            Alllanguages.append(language)
    if i == 0:
        Commonlanguages = Languages
    else:
        Commonlanguages = [lang for lang in Commonlanguages if lang in Languages]
print("Number of languages everyone speaks:", len(Commonlanguages))
print("Languages spoken by everyone in the group: ", end="")
for i in range(len(Commonlanguages)):
    if i > 0:
        print(", ", end="")
    print(Commonlanguages[i], end="")
print()
print("Number of total languages spoken in the group:", len(Alllanguages))
print("Languages spoken in the group: ", end="")
for i in range(len(Alllanguages)):
    if i > 0:
        print(", ", end="")
    print(Alllanguages[i], end="")
print()
