previous_num = 0
for i in range(1, 11):
    if i == 1:
        print("Previous number: ", previous_num)
    print("Current number: ", i)
    sum = previous_num + i
    print("Sum of current and previous number: ", sum)
    previous_num = i