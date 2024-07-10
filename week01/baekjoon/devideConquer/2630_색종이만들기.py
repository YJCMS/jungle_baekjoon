import sys 

def square_divide(x, y, n):
    global w, b
    first_color = square[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if first_color != square[i][j]:
                square_divide(x, y, n//2)
                square_divide(x, y+n//2, n//2)
                square_divide(x+n//2, y, n//2)
                square_divide(x+n//2, y+n//2, n//2)
                return
    if first_color == 0:
        w += 1
    else: 
        b += 1

n = int(sys.stdin.readline())
square = []
for i in range(n):
    square.append(list(map(int, sys.stdin.readline().split())))
w = 0
b = 0
square_divide(0, 0, n)
print(w)
print(b)