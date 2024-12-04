list_a = []
list_b = []
answer = 0

with open("day1_data.txt") as data:
    for i in data:
        list_a.append(int(i[:5]))
        list_b.append(int(i[8:13]))

for number_a in list_a:
    multiplier = 0
    for number_b in list_b:
        if number_a == number_b:
            multiplier += 1
    
    answer += number_a * multiplier

print(answer)