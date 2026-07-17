# mashq-1
fruits = ['apple', 'banana', 'orange', 'Mango', 'Kiwi']
print(f'Fruits list: {fruits}')
# mashq-2
numbers = [10, 20, 30, 40, 50]
print(f"First Item: {numbers[0]}")
print(f"Middle Item: {numbers[2]}")
print(f"Last Item: {numbers[-1]}")
# mashq-3
colors = ["Red", "Blue", "Green"]
colors.append("Yellow")
print(f"Colors list after appending: {colors}")
# mashq-4
animals = ["Cat", "Dog", "Rabbit", "Horse"]
animals.remove("Rabbit")
print(f"Animals list: {animals}")
# mashq-5
countries = ["Uzbekistan", "Kazakhstan", "Russia"]
countries[-1] = "Turkey"
print(f"Countries list: {countries}")
# mashq-6
students = ["Ali", "Vali", "Hasan", "Husan", "Aziza"]
print(f"Number of students: {len(students)}")
#mashq-7
numbers = [45, 12, 89, 3, 67, 21]
numbers.sort()
print(f"Sorted List: {numbers}")
#mashq-8
scores = [78, 95, 67, 88, 100, 56]
print(f"Highest Score: {max(scores)}")
print(f"Lowest Score: {min(scores)}")
#mashq-9
numbers = [5, 10, 15, 20, 25]
print(f"Sum of numbers: {sum(numbers)}")
# mashq-10
empty_list = []
input_1 = input("Enter a number: ")
input_2 = input("Enter another number: ")
input_3 = input("Enter another number: ")
input_4 = input("Enter another number: ")
input_5 = input("Enter another number: ")
empty_list.append(int(input_1))
empty_list.append(int(input_2))
empty_list.append(int(input_3))
empty_list.append(int(input_4))
empty_list.append(int(input_5))
print(f"Empty List: {empty_list}")
print(f"Max number: {max(empty_list)}")
print(f"Min number: {min(empty_list)}")
print(f"Sum of numbers: {sum(empty_list)}")