def is_year_leap(data):
    if data % 4 == 0:
        return True
    else:
        return False


year = int(input("Укажите год: "))

result = is_year_leap(year)
print(f"Год {year}: {result}")
