# 1
numbers = input("�������� ������ �� �����: ").split()
print("������� �� ��������:", numbers[0])
print("������� �� ����:", numbers[-1])

# 2
numbers = input("�������� ������ �� �����: ").split()
print("������� �� �������:", len(numbers))

# 3
numbers = [int(x) for x in input("�������� ������ �� �����: ").split()]
print("������ �� ������ ��������:", sum(numbers))

# 4
numbers = [int(x) for x in input("�������� ������ �� �����: ").split()]
print("��������� �:", min(numbers))

# 5
numbers = [int(x) for x in input("�������� ������ �� �����: ").split()]
print("���������� �:", max(numbers))

# 6
numbers = input("�������� ������ �� �����: ").split()
reversed_numbers = numbers[::-1]
print("������� ���������:", ' '.join(reversed_numbers))

# 7
numbers = [int(x) for x in input("�������� ������ �� �����: ").split()]
odd_index_elements = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]
print("���������� �� ������� �������:", odd_index_elements)

# 8
numbers = [int(x) for x in input("�������� ������ �� �����: ").split()]
average = sum(numbers) / len(numbers)
print("������ ����������� �� ����������:", average)

# 9
numbers = [int(x) for x in input("�������� ������ �� �����: ").split()]
count_zeros = numbers.count(0)
print("���� �� ������ � �������:", count_zeros)

# 10
numbers = [int(x) for x in input("�������� ������ �� �����: ").split()]
positive_numbers = [x for x in numbers if x > 0]
print("������������� �����:", positive_numbers)

# 11
numbers = [int(x) for x in input("�������� ������ �� �����: ").split()]
larger_than_previous = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]
print("���������� ��-������ �� �����������:", larger_than_previous)

# 12
numbers = [int(x) for x in input("�������� ������ �� �����: ").split()]
unique_elements = set(numbers)
print("���� �������� ��������:", len(unique_elements))

# 13
numbers = [int(x) for x in input("�������� ������ �� �����: ").split()]
index_to_remove = int(input("�������� ������ �� ����������: "))
if 0 <= index_to_remove < len(numbers):
    del numbers[index_to_remove]
print("���������� ������:", numbers)

# 14
numbers = [int(x) for x in input("�������� ������ �� �����: ").split()]
modified_numbers = [x - 1 if x % 2 == 0 else x + 1 if x != 0 else 0 for x in numbers]
print("�������� ������:", modified_numbers)

# 15
numbers = [int(x) for x in input("�������� ������ �� �����: ").split()]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
max_frequency = max(frequency.values())
most_common = min([key for key, value in frequency.items() if value == max_frequency])
print("���-����� ��������� �������:", most_common)

# 16
numbers = input("�������� ������ �� �����: ").split()
print("������� �� ��������:", numbers[0])
print("������� �� ����:", numbers[-1])

# 17
numbers = [int(x) for x in input("�������� ������ �� �����: ").split()]
number_to_remove = int(input("�������� ����� �� ����������: "))
filtered_numbers = [x for x in numbers if x != number_to_remove]
print("���������� ������:", filtered_numbers)

# 18
numbers = [int(x) for x in input("�������� ������ �� �����: ").split()]
swapped_pairs = [numbers[i + 1] if i % 2 == 0 and i + 1 < len(numbers) else numbers[i] for i in range(len(numbers))]
print("��������� ������ ��������:", swapped_pairs)

# 19
numbers = [int(x) for x in input("�������� ������ �� �����: ").split()]
even_numbers = [x for x in numbers if x != 0 and x % 2 == 0]
print("��� ������ � ����� �����:", even_numbers)

# 20
numbers = [int(x) for x in input("�������� ������ �� �����: ").split()]
average = sum(numbers) / len(numbers)
larger_than_average = [x for x in numbers if x > average]
print("�������� ��-������ �� �������� �����������:", larger_than_average)

