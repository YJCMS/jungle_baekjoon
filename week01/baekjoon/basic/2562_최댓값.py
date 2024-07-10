list_n = []
for i in range(9) :
    list_n.append(int(input()))
print(max(list_n))
print(list_n.index(max(list_n))+1)
