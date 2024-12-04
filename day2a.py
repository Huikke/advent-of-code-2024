answer = 0

with open("day2_data.txt") as data:
    for line in data:
        report = [int(i) for i in line.split(" ")]
        
        first = True
        direction = 0
        safe = True
        for level in report:
            if first:
                value = level
                first = False
                continue
            
            diff = value - level
            if diff <= 3 and diff >= -3 and diff != 0:
                if direction == 0:
                    direction = diff / abs(diff)
                elif diff > 0 and direction == 1:
                    pass
                elif diff < 0 and direction == -1:
                    pass
                else:
                    safe = False
                    break
                value = level
            else:
                safe = False
                break
        if safe:
            answer += 1

print(answer)