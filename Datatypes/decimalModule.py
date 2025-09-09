import decimal

a = 1.1 + 2.2
b = 3.3

print(a == b)

c = decimal.Decimal("1.1") + decimal.Decimal("2.2")
d = decimal.Decimal("3.3")

print(c == d)