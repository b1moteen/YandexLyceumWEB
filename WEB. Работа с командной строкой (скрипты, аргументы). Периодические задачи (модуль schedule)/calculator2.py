import sys
summ = 0
if len(sys.argv) == 1:
    print("NO PARAMS")
else:
    for i in range(1, len(sys.argv)):
        if sys.argv[i].isdigit():
            if i % 2 == 0:
                summ -= int(sys.argv[i])
            else:
                summ += int(sys.argv[i])
    print(summ)