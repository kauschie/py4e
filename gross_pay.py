def computepay(hours, rate):
    if hours > 40:
        adjHours = hours - 40
        pay = (40*rate) + (adjHours*rate*adjRate)
        return pay
    else:
        pay = hours * rate
        return pay


adjRate = 1.5
adjHours = 0

try:
    hours = int(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print('Error, please enter numeric input')
    quit()

pay = computepay(hours, rate)
print('Pay:', pay)
