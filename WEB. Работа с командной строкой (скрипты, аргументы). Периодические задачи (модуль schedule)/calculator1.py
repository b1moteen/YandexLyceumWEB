import sys

if len(sys.argv) != 3:
    print(0)
elif sys.argv[1].isdigit() and sys.argv[2].isdigit():
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print(num1 + num2)
else:
    print(0)
