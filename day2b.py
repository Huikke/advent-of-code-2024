answer = 0

def analyze(report):
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
        return True

with open("day2_data.txt") as data:
    for line in data:
        report = [int(i) for i in line.split(" ")]

        if analyze(report):
            answer += 1
        else:
            for i in range(len(report)):
                damp_report = report.copy()
                del damp_report[i]
                if analyze(damp_report):
                    answer +=1
                    break
                else:
                    continue

print(answer)