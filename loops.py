end = False
while end != True:
    user_input = input("Svetafor rangini kiriting:").lower()
    if user_input == 'qizil':
        print("raxmat to'g'ri keldi")
    elif user_input == 'sariq':
        print("raxmat to'g'ri keldi")
    elif user_input == 'yashil':
        print("raxmat to'g'ri keldi")
    else:
        print('xato rang kiritngdingz')
        print(user_input)
        end = True
