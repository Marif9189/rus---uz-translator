# Ruscha - O'zbekcha tarjimon (oddiy lug'at asosida)

lugat = {
    "привет": "salom",
    "как": "qanday",
    "ты": "sen",
    "здравствуйте": "assalomu alaykum",
    "пока": "xayr",
    "спасибо": "rahmat",
    "друг": "do'st",
    "вода": "suv",
    "дом": "uy",
    "работа": "ish"
}

def tarjima(soz):
    soz = soz.lower()
    if soz in lugat:
        return lugat[soz]
    else:
        # agar lug‘atda topilmasa teskari tarjima qidiramiz
        for rus, uz in lugat.items():
            if uz == soz:
                return rus
        return "❌ So'z topilmadi"

print("Ruscha ↔ O'zbekcha tarjimon")
while True:
    kirit = input("So'z kiriting (chiqish uchun 'exit'): ")
    if kirit == "exit":
        break
    print("Tarjima:", tarjima(kirit))
