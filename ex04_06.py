def computepay(hours, rate):
    if hours > 40:
        ot = hours-40.0
        pay = hours*rate + (ot*0.5)*rate
    else:
        pay = hours*rate
    return pay


hours = input('Enter hours: ')
rate = input('Enter rate: ')
try:
    fh = float(hours)
    fr = float(rate)
except:
    print('numbers required')
    quit()

pay = computepay(fh,fr)

print('Pay:',pay)
