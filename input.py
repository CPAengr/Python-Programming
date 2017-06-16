def currency_converter(rate, euros):
    dollars = rate*euros
    return dollars


r = input("Enter rate: ")
e = input("Enter euros: ")
print(currency_converter(int(r), int(e)))
