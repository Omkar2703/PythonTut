# Printing omkar 5 times using recursion
def f(i, n):
    if i>n :
        return
    print("Omkar")
    f(i+1, n)
n = int(input("How many times do you wanted to print?"))
i=1
f(i, n)

# #Printng (1 to N) numbers

# def f(i, n):
#     if i>n:
#         return
#     print(i)
#     f(i+1, n)
# n = int(input("Enter the value of N: "))
# i = 1
# f(i, n)

# # Printing number from N to 1
# def f(i, n):
#     if i<1:
#         return
#     print(i)
#     f(i-1, n)
# n = int(input("Enter the value of N: "))
# f(n, n)

# #Printing Numbers from 1 to N Using BackTracking
# def f(i, n):
#     if i<1:
#         return
#     f(i-1, n)
#     print(i)
# i = 1
# n = int(input("Enter the value of N: "))
# f(n, n)

# # Printing Numbers from N to 1 Using BackTracking
# def f(i,n):
#     if i>n:
#         return
#     f(i+1, n)
#     print(i)
# i = 1
# n = 5
# f(i, n)