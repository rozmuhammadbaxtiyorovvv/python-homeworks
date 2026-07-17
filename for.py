# mashq-1
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

# mashq-2
fruits = ["olma", 'anjir', 'ananans', "banan", "anor", "shaftoli"]
for fruit in fruits:
    print(fruit)

# mashq-3
text = "Python dasturlash tili"
for letter in text: 
    print(letter)
# mashq-4
for i in range(5):
    print(i)
# mashq-5
for i in range(1,6):
    print(i)
# mashq-6
for i in range(0, 10, 2):
    print(f"Juft son: {i}")
# mashq-7
for i in range(10, 0, -1):
    print(f"Orqaga: {i}")
# mashq-8
summa = 0
for number in numbers:
    summa += number
print(f"Sonlar yig'indisi: {summa}")
# mashq-9
for fruit in fruits:
    print(f"Length of {fruit} is {len(fruit)}")
# mashq-10
vowels = ["a", "e", "i", "o", "u"]
for letter in text:
    if letter.lower() in vowels:
        print(f"{letter} is a vowel")
# mashq-11
for num in range(0, 11):
    print(f"{num} ning kvadrati: {num ** 2}")
# mashq-12
for num in range(1, 11):
    print(f"{num} ning kubi {num ** 3}")
# mashq-15
for fruit in fruits:
    if fruit.startswith("a"):
        print(f"{fruit} 'a' harfi bilan boshlanadi")
# mashq-16
count = 0
for letter in text:
    if 'o' in letter.lower():
        count += 1
print(f"Matnda 'o' harfi {count} marta uchraydi")
# mashq-17