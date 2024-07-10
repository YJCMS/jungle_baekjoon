import sys

num_list = []
for i in range(9):
    num_list.append(int(sys.stdin.readline()))
    
num_list.sort()
sum = sum(num_list)
a = 0
b = 0

for i in range(len(num_list)):
    for j in range(i+1, len(num_list)):
        if sum - num_list[i] - num_list[j] == 100 :
            a = num_list[i]
            b = num_list[j]

num_list.remove(a)
num_list.remove(b)

for i in num_list:
    print(i)