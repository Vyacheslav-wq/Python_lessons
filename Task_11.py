# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

# number = int(input("Введите число: "))

# i = 1
# res = 1

# while i <= number:
#     res *= i
#     i += 1

# print(f"{number}! равен {res}")


number = int(input("Введите число: "))
fact = number
res = 1

while number > 1:
    res *= number
    number -= 1

print(f"{fact}! равен {res}")

# n = int(input('Введите число фибоначи: '))
# a = int(input('Введите число Фибоначчи: '))

# n1 = 0
# n2 = 1
# r = 1
# count = 3

# while r < a:
#     n1 = n2
#     n2 = r
#     r = n1 + n2
#     count += 1

# if a != r:
#     count = -1
# print(count)

a = int(input('Введите число Фибоначчи: '))

n1 = 1
n2 = 2
count = 4

while n2 < a:
    n2, n1 = n1 + n2, n2
    count += 1

if a != n2:
    count = -1
print(count)


