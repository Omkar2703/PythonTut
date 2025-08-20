# paramiterised recusion
# Print the sum of number N numbers

# def f(i, sum):
#     if i<0:
#         print(sum)
#         return
#     f(i-1, sum + i)
# n = int(input("Enter the value of N: "))
# f(n, 0)

# Factorial of N numbers
def f(i, fact):
    if i<=0:
        print(fact)
        return
    f(i-1, i*fact)
n = 4
f(n, 1)

# functional recursion
# Print the sum of number N numbers

# def f(n):
#     if n<0:
#         return 0
#     return n + f(n-1)
# n = 4
# print(f(n))

# factorial of N numbers
# def f(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * f(n-1)
# n = 4
# print(f(n))