word = str(input("Enter Word: "))
letter = str(input("Enter letter to search from work: "))
count = 0

for i in word:
    if i == letter:
        count +=1

print (f"letter '{letter} was repeated {count} times in the word")