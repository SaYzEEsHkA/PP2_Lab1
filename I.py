n = int(input())
a = []
i = int()

if n==0:
    exit()

while len(a)<n:
    a.append(input())

while i<len(a):
    if "@gmail.com" in a[i]:
        print(a[i][:-10])
    i=i+1
