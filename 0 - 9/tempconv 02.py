cel = int(input('Enter temperature is C° (number only):'))

far = (cel * 9/5) + 32
kelvin = cel + 273.15 

print(f'{cel} C° is equal to {far} F° (Fahrenheits).' )
print(f'{cel} C° is equal to {kelvin} K (Kelvins).')