import sys

def move(no, x, y):
    if no > 1 :
        move(no-1, x, 6-x-y)
    print(x, y)
    if no > 1:
        move(no-1, 6-x-y, y)

n = int(sys.stdin.readline())
print(2**n-1)
if n <=20 :
    move(n, 1, 3)