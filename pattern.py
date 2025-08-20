def print1():
    for i in range(0, n):
        for j in range(0, n):
            print("*", end=" ")
        print()
def print2():
    for i in range(0, n):
        for j in range(0, i+1):
            print("*", end=" ")
        print()
def print3():
    for i in range(1, n):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
def print4():
    for i in range(1, n):
        for j in range(1, i+1):
            print(i, end=" ")
        print()
def print5():
    for i in range(1, n):
        for j in range(1, n-i+1):
            print("*", end=" ")
        print()
def print6():
    for i in range(1, n):
        for j in range(1, n-i+1):
            print(j, end=" ")
        print()
def print7():
    for i in range(1, n):
        for j in range(1, n-i+1):
            print(i, end=" ")
        print()
def print8():
    for i in range(0, n):
        for j in range(0, i+1):
            print(" ", end=" ")
        for j in range(0, 2*n-(2*i+1)):
            print("*", end=" ")
        print()
n=4
# print1()
print8()


    