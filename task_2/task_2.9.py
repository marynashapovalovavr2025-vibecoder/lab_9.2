n = int(input())
i = 0
while(i <= n):
    s = str(i)
    if (s == s[::-1]):
        print(i)
    i+=1