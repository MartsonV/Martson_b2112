from random import randint
lst = [randint(-10, 10) for i in range (20)]
print(lst)

sum_negativ = 0

for num in lst:
    if num < 0: sum_negativ += num
print("Sum negativ item list: ", sum_negativ)


