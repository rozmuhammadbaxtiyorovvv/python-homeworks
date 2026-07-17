# append()
cars = []
cars.append("Spark")
cars.append("BYD")
print(cars)

# insert()
cars.insert(1, 'Damas')
cars.insert(2, "Cobalt")
print(cars)

# pop()
my_car = cars.pop(0)
dream_car = cars.pop(-1)
print(f"I have a {my_car}")
print(f"I would like to purchase a {dream_car} one day")

# remove()
friends = ['john doe', 'elon musk', 'bill gates', 'jeff bezos']
friends.remove('john doe')
friends.remove('bill gates')
print(friends)

# del
football_players = ['cristano ronaldo', 'lionel messi', 'neymar jr', 'kylian mbappe', 'robert lewandowski', 'lammin yamal']
del football_players[0]
del football_players[3]
print(football_players)

# sort()
guests = ['elon musk', 'stive jobs', 'bill gates', 'jeff bezos', 'mark zuckerberg', 'larry page', 'sergey brin', 'tim cook', 'pavel durov', 'jack dorsey']
guests.sort()
print(f'sorted order: {guests} \n')
guests.sort(reverse=True)
print(f'reversed order: {guests}')

# reverse()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
guests.reverse()
print(f'reverse() method: {guests}')
numbers.reverse()
print(f'reverse() method: {numbers}')

# len()
print(f'length of guests list: {len(guests)}')
print(f"Length of football_players list: {len(football_players)}")

# max & min
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")

# copy()
guests_copy = guests.copy()
football_p_copy = football_players.copy()
guests_copy.append("Dilshoddd")
guests_copy.insert(0, "Qorni Katta")
print(f"COPY OF GUESTS: {guests_copy}")
print(f"ORIGINAL LIST OF GUESTS {guests}")
football_p_copy.append("Son")
football_p_copy.append("ozil")
print(f"COPY OF FOOTBALL PLAYERS {football_p_copy}")
print(f"ORIGINAL LIST OF FOOTBALL PLAYERS {football_players}")

# index()
print(f"GUESTS INDEX ELON MUSK's INDEX: {guests.index('elon musk')}")
print(f"OZIL's INDEX {football_p_copy.index('ozil')}")

# clear()
hello_in_forgein = ['hello', 'hola', 'salom', 'bonjour']
random_num = list(range(1, 10))
print(hello_in_forgein)
print(random_num)
hello_in_forgein.clear()
random_num.clear()
print(f"hello_in_forgein: {hello_in_forgein}, random_num:{random_num}")

# extend()

empty_list = []
english_vocab = ("hello", "how are u", "whats ur name", "where are u from")
uzbek_vocab = ("salom", 'nichiksan', 'oding kim', 'nedansan')
empty_list.extend(english_vocab)
empty_list.extend(uzbek_vocab)
print(empty_list)

# count()
numbers = list(range(0, 100))
print(f"HOW MANY 9 in the 100: {numbers.count(9)}")
print(f"HOW MANY 11 in the 100: {numbers.count(11)}")

