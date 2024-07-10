n = int(input())
for i in range(n) :
    a, s= input().split()
    for k in range(len(s)):
        print(int(a) * s[k], end='')
    print()