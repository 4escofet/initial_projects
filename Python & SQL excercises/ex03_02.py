hours = input('Enter hours: ')
rate = input('Enter rate: ')
try:
    fh = float(hours)
    fr = float(rate)
except:
    print('numbers required')
    quit()
if fh > 40:
    ot = fh-40.0
    pay = fh*fr + (ot*0.5)*fr
else:
    pay = fh*fr
print('Pay:',pay)
