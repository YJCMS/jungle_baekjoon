import sys

n = int(sys.stdin.readline())
timetable = []

for i in range(n):
    s, f = map(int, sys.stdin.readline().split())
    timetable.append([s, f])
    
timetable.sort(key = lambda x : (x[1], x[0]))

cnt = 1
end = timetable[0][1]
for i in range(1, n):
    if timetable[i][0] >= end:
        end = timetable[i][1]
        cnt += 1

print(cnt)