from random import randint
lst = [randint(-10, 10) for i in range (20)]
print(lst)

sum_negativ = 0

for num in lst:
    if num < 0: sum_negativ += num
print("Sum negativ item list: ", sum_negativ)

sum_of_even = 0
for num in lst:
   if num %2 == 0:
       sum_of_even =+ num
print("Sum of even item list: ", sum_of_even)


sum_of_odd = 0
for num in lst:
    if num % 2 != 0:
        sum_of_odd += num
print("Sum of even item list: ", sum_of_odd)

sum_elements_mult_3 = 0
for i in range(len(lst)):
   if i % 3 == 0:
    sum_elements_mult_3 += lst[i]
print("the sum of elements that are multiples of 3:", sum_elements_mult_3)

min_value_list = min(lst)
max_value_list = max(lst)
