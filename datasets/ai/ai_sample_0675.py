def convertTemp(temp, fromUnit, toUnit):
    if fromUnit == 'C':
        if toUnit == 'F':
            temp = temp * (9/5) + 32
        elif toUnit == 'K':
            temp += 273.15
    elif fromUnit == 'F':
        if toUnit == 'C':
            temp = (temp - 32) * (5/9)
        elif toUnit == 'K':
            temp = (temp - 32) * (5/9) + 273.15
    elif fromUnit == 'K':
        if toUnit == 'C':
            temp -= 273.15
        elif toUnit == 'F':
            temp = (temp - 273.15) * (9/5) + 32

    return temp

temp = 100
print("In Celsius:", convertTemp(temp, 'F', 'C'))
print("In Fahrenheit:", convertTemp(temp, 'C', 'F'))
print("In Kelvin:", convertTemp(temp, 'C', 'K'))