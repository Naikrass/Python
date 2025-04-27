year = int(input("Введите год:"))


def is_year_leap(year):
    return year % 4 == 0


print(f"год {year}: {is_year_leap(year)}")
