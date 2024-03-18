# 1
numbers = input("Въведете списък от числа: ").split()
print("Елемент от началото:", numbers[0])
print("Елемент от края:", numbers[-1])

# 2
numbers = input("Въведете списък от числа: ").split()
print("Дължина на списъка:", len(numbers))

# 3
numbers = [int(x) for x in input("Въведете списък от числа: ").split()]
print("Сумата на всички елементи:", sum(numbers))

# 4
numbers = [int(x) for x in input("Въведете списък от числа: ").split()]
print("Минимумът е:", min(numbers))

# 5
numbers = [int(x) for x in input("Въведете списък от числа: ").split()]
print("Максимумът е:", max(numbers))

# 6
numbers = input("Въведете списък от числа: ").split()
reversed_numbers = numbers[::-1]
print("Списъка наобратно:", ' '.join(reversed_numbers))

# 7
numbers = [int(x) for x in input("Въведете списък от числа: ").split()]
odd_index_elements = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]
print("Елементите на нечетни индекси:", odd_index_elements)

# 8
numbers = [int(x) for x in input("Въведете списък от числа: ").split()]
average = sum(numbers) / len(numbers)
print("Средно аритметично на елементите:", average)

# 9
numbers = [int(x) for x in input("Въведете списък от числа: ").split()]
count_zeros = numbers.count(0)
print("Брой на нулите в списъка:", count_zeros)

# 10
numbers = [int(x) for x in input("Въведете списък от числа: ").split()]
positive_numbers = [x for x in numbers if x > 0]
print("Положителните числа:", positive_numbers)

# 11
numbers = [int(x) for x in input("Въведете списък от числа: ").split()]
larger_than_previous = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]
print("Елементите по-големи от предходните:", larger_than_previous)

# 12
numbers = [int(x) for x in input("Въведете списък от числа: ").split()]
unique_elements = set(numbers)
print("Брой различни елементи:", len(unique_elements))

# 13
numbers = [int(x) for x in input("Въведете списък от числа: ").split()]
index_to_remove = int(input("Въведете индекс за премахване: "))
if 0 <= index_to_remove < len(numbers):
    del numbers[index_to_remove]
print("Резултатен списък:", numbers)

# 14
numbers = [int(x) for x in input("Въведете списък от числа: ").split()]
modified_numbers = [x - 1 if x % 2 == 0 else x + 1 if x != 0 else 0 for x in numbers]
print("Променен списък:", modified_numbers)

# 15
numbers = [int(x) for x in input("Въведете списък от числа: ").split()]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
max_frequency = max(frequency.values())
most_common = min([key for key, value in frequency.items() if value == max_frequency])
print("Най-често срещаният елемент:", most_common)

# 16
numbers = input("Въведете списък от числа: ").split()
print("Елемент от началото:", numbers[0])
print("Елемент от края:", numbers[-1])

# 17
numbers = [int(x) for x in input("Въведете списък от числа: ").split()]
number_to_remove = int(input("Въведете число за премахване: "))
filtered_numbers = [x for x in numbers if x != number_to_remove]
print("Резултатен списък:", filtered_numbers)

# 18
numbers = [int(x) for x in input("Въведете списък от числа: ").split()]
swapped_pairs = [numbers[i + 1] if i % 2 == 0 and i + 1 < len(numbers) else numbers[i] for i in range(len(numbers))]
print("Разменени двойки елементи:", swapped_pairs)

# 19
numbers = [int(x) for x in input("Въведете списък от числа: ").split()]
even_numbers = [x for x in numbers if x != 0 and x % 2 == 0]
print("Нов списък с четни числа:", even_numbers)

# 20
numbers = [int(x) for x in input("Въведете списък от числа: ").split()]
average = sum(numbers) / len(numbers)
larger_than_average = [x for x in numbers if x > average]
print("Елементи по-големи от средното аритметично:", larger_than_average)

