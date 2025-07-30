from smartphone import Smartphone

catalog = [
    Smartphone("Techo", "SPARK GO", "+79051261264"),
    Smartphone("Apple", "iPhone 11", "+79051251254"),
    Smartphone("Xiaomi", "Redmi realme", "+79051241244"),
    Smartphone("Samsung", "A 32", "+79051231234")
]

for phone in catalog:
    print(f"{phone.brend} - {phone.mod}. {phone.phone_num}")
