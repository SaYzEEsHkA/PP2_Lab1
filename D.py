x = int(input()) #our number
z = input() #command that convert

result = int()

if z == 'k':
    c = int(input()) #how many digits
    result = (x / 1024)
    print(round (result, c))

elif z == 'b':
    result = (x * 1024)
    print (result)
