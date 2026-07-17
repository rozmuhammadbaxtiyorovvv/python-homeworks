def tugilgan_yil():
    ism = input("Ismingizni kiriting: ")
    yosh = int(input("Yoshingizni kiriting: "))
    yil = 2026 - yosh
    print(ism, "ning tug'ilgan yili:", yil)


def kvadrat_kub():
    son = int(input("Son kiriting: "))
    print("Kvadrati:", son * son)
    print("Kubi:", son * son * son)


def juft_yoki_toq():
    son = int(input("Son kiriting: "))
    if son % 2 == 0:
        print("Juft son")
    else:
        print("Toq son")


def katta_son():
    a = int(input("Birinchi sonni kiriting: "))
    b = int(input("Ikkinchi sonni kiriting: "))

    if a > b:
        print(a)
    elif b > a:
        print(b)
    else:
        print("Sonlar teng")


def daraja(x, y=2):
    print(x ** y)


def bolinish():
    son = int(input("Son kiriting: "))

    for i in range(2, 11):
        if son % i == 0:
            print(son, i, "ga qoldiqsiz bo'linadi")
        else:
            print(son, i, "ga qoldiqsiz bo'linmaydi")


tugilgan_yil()
kvadrat_kub()
juft_yoki_toq()
katta_son()
daraja(5)
daraja(5, 3)
bolinish()