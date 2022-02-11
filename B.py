s = input()

i = int()

sum = int()

while i<len(s):
    sum = sum + ord(s[i])
    i = i+1

if sum>300:
    print ("It is tasty!")
else:
    print ("Oh, no!")
