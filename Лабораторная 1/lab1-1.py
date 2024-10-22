numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

modified_numbers = numbers[:4] + numbers[5:]

average_of_numbers = round((sum(modified_numbers)) / len(numbers), 2)

numbers[4] = average_of_numbers

print("Измененный список:", numbers)
