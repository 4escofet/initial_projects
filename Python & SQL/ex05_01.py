count = 0
tot = 0.0
smallest = None
largest = None
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
        print(sval)
    except:
        print('Invalid input')
        continue
    if smallest is None and largest is None:
        smallest = fval
        largest = fval

    if fval < smallest:
        smallest = fval
    if fval > largest:
        largest = fval
    #print('Cantidad de ingresos: ',num)
    count = count +1
    tot = tot + fval
    #print('Suma acumulada: ',tot)


print('Total ',tot, 'Count ',count, 'largest ',largest, 'smallest',smallest)
