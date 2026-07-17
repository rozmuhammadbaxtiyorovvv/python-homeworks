my_list = []
number = [1, 2, 3, 4, 5]
fruits = ['apple', 'bannana', 'cherry']

print(f"Numbers List: {number}")
print(f"Fruits List: {fruits}")
print(f"Length of numbers List: {len(number)}")
print(f"Length of fruits List: {len(fruits)}")


print(f"First element of numbers List: {number[0]}")
print(f"Last element of fruits List: {fruits[-1]}")
print(f"Second element of numbers List: {number[1]}")
number[1] = 10
print(f"Updated numbers List element second: {number[1]}")

fruits.append('orange')


fruits.insert(0, 'grape')
fruits.remove('bannana')
# deleting the last element of numbers
number.pop()

check_apple = 'apple' in fruits
print(f"Is apple in fruits list?: {check_apple}")

check_7 = 7 in number
print(f"Is 7 in numbers list?: {check_7}")

mixed_list = ['john doe', 25, 'new york USA', 5000, 'truck dispatcher', True]
colors = ['red', 'green', 'blue', 'yellow', 'black']
new_colors = colors.copy()
new_colors.clear()

combined_list = number + fruits


repeated_numbers = number + number + number
fruits.append('apple')
fruits.sort()
number.reverse()


print(f"Updated Fruits List: {fruits}")
print(f"Updated Numbers List: {number}")
print(f"Mixed List: {mixed_list}")
print(f"Colors List: {colors}")
print(f"New Colors List: {new_colors}")
print(f"Combined List: {combined_list}")
print(f"Repeated Numbers List: {repeated_numbers}")

print(f"in the fruit list we have {fruits.count('apple')} apple(s)")

print(f"cherry's index is {fruits.index('cherry')}")