"""I have a project Idea for this file"""
def split_and_join(line):
    line = line.replace(" ","-")
    return(line) 
 
line="this is a string"
print(split_and_join(line))





def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')

