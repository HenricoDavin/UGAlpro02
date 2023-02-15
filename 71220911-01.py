#input
x = int(input('x:'))
y = int(input('y: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))

#proses
jarak = ((x-x2)**2 + (y-y2)**2)**0.5
jarak = int(jarak*10)/10

#output
print ('Jarak antara titik adalah= {}'.format(jarak))