s = input()
t = input()
result = []

i = int()
while i<len(s):
    if s[i]==t:
        result.append(i)
    i = i+1
import time
print (result[0], end=' ')
time.sleep(0.1)
if len(result)>1:
    print (result[len(result)-1], end='')
    time.sleep(0.1)
