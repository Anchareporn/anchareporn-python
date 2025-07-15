print("===BMI Calculator===")

while True:
    try:
        kilo = float(input('Enter you weight:'))
        if kilo > 0:
            break
        else:
            print('Please try again.')
    except ValueError:
        print("Invalid kilo")

while True:
    try:
        heigth = float(input("enter  you heigth"))
        if heigth > 0:
            heigth = heigth / 100
            break
        else:
            print('Please try again.')
    except ValueError:
        print("Invalid heigth")

bmi = kilo / (heigth ** 2)

if bmi >= 30.0:
    print('Obase')
elif bmi >= 25.0:
    print('Overweigth')
elif bmi >= 18.5:
    print('Normal weigth')
else:
    print('Under weigth')

print(f'you weigth :{kilo:.2f}')
print(f'you heigth :{heigth:.2f}')
print(f'you bmi is :{bmi:.2f}')
