n = int(input())
hour, min = 0, 0
answer = 0
hour_has_three, min_has_three = False, False

while(1):
    if hour == 3 or hour%10 == 3 or int(hour/10) == 3:
        hour_has_three = True

    for j in range(60):
        if j == 3 or j%10 == 3 or int(j/10) == 3 or min_has_three or hour_has_three:
            answer += 1
    
    min += 1
    min_has_three = False

    if min == 3 or min%10 == 3 or int(min/10) == 3:
        min_has_three = True
    
    if min == 60:
        min = 0
        hour += 1
        hour_has_three = False

        if hour > n:
            break

print(answer)


