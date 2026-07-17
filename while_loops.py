togri_ranglar = ["qizil", "sariq", "yashil"]

while True:
    rang = input("Svetafor qaysi rangda? ").lower()
    
    if rang in togri_ranglar:
        print("rahmat, to'g'ri keladi")
        break
    else:
        print("Xato rang! Iltimos, qizil, sariq yoki yashil rangni kiriting.\n")


dostlar = []

while True:
    ism = input("Do'stingizning ismini kiriting (to'xtatish uchun 'stop' deb yozing): ").strip()
    
    if ism.lower() == "stop":
        break
    
    if ism != "":
        dostlar.append(ism)
    else:
        print("Ism bo'sh bo'lishi mumkin emas!")

print("\nSizning do'stlariz ro'yxati:")
for d in dostlar:
    print(f"- {d}")

KURS = 12600

print("--- SO'M -> USD Kalkulyatori ---")
print("Chiqish uchun 'exit' deb yozing.\n")

while True:
    qiymat = input("Siz almashtirmoqchi bo'lgan so'm miqdorini kiriting: ").strip()
    
    if qiymat.lower() == "exit":
        print("Dastur tugatildi. Salomat bo'ling!")
        break
        
    if qiymat.isdigit():
        som = float(qiymat)
        dollar = som / KURS
        print(f"Natija: {som:,.0f} so'm = {dollar:.2f} USD\n")
    else:
        print("Iltimos, faqat butun raqam kiriting yoki dasturdan chiqish uchun 'exit' deb yozing.\n")
