numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_index = 4
excluded_index = 5

modified_numbers = numbers[:missing_index] + numbers[excluded_index:]
average_of_numbers = round((sum(modified_numbers)) / len(numbers), 2)

numbers[missing_index] = average_of_numbers

print("Измененный список:", numbers)
