n = int(input())
f = int(input())

if n<=500:
    for i in range (2, n):
        if (n%i)!=0:
            if (f%2)==0:
                flag = 'true'
    if flag == 'true':
        print("Good job!")
else:
    print("Try next time!")
