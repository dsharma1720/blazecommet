n = int(input("enter the number of rows : "))
for i in range(0, n):

    for j in range(i, n):
        print("", end=" ")

    for j in range(i):
        print("*", end="")

    for j in range(i+1):
        print("*", end="")

    print()