list_a = []
list_b = []
answer = 0

with open("day1_data.txt") as data:
    for i in data:
        list_a.append(int(i[:5]))
        list_b.append(int(i[8:13]))
    
list_a.sort()
list_b.sort()

for i in range(len(list_a)):
    if list_a[i] > list_b[i]:
        answer += list_a[i] - list_b[i]
    else:
        answer += list_b[i] - list_a[i]

print(answer)