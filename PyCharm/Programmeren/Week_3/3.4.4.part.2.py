maanden = ("januari", "februari", "maart", "april", "mei", "juni")
for month in maanden:
    print ("Maanden die bestaan zijn", month)

print("_")

total = 0
product = 1
numbers = (12, 10, 32, 3, 66, 17, 42, 99, 20)
for number in numbers:
    total += number
    product *= number
    print(number, (number**0.5))
    print(total)
    print(product)


