def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}") #This will print 0

my_list_with_zero = [10,0,20,30]
average_zero = calculate_average(my_list_with_zero)
print(f"The average of a list with zero is: {average_zero}") #This will print 15.0