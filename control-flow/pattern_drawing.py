size = int(input("Enter the size of the pattern: "))
width = size

while size > 0:
    for row in range(1, width+1):
        print("*", end="")
    print(" ")
    size -= 1
