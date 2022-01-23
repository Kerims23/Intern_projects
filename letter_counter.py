word = str(input("Enter Word: "))
letter = str(input("Enter letter to search from work: "))
count = 0

for i in word:
    if i == letter:
        count +=1