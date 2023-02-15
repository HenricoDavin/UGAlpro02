#input
input_inch = int(input('Masukkan inch: '))

#proses
_feet = 12
_yard = 3*_feet
_mile = 1760*_yard

mile = input_inch // _mile
yard = (input_inch - mile*_mile)//_yard
feet = (input_inch - mile*_mile - yard*_yard) // _feet
inch = (input_inch - mile*_mile - yard*_yard - feet*_feet)

#output
print (f'{mile} mile {yard} yard {feet} feet {inch} inch')