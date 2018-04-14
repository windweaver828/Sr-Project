from random import gauss, randint

time = 0
results=[]

def biased_random(minimum, mean, maximum, stdev):
    value = gauss(mean, stdev)
    if '-' in str(value):
        value = gauss(mean, stdev)
    else:
        return value

def parts_order(n, values, error):
    determine = biased_random(126, 322, 484, 91)
    order = biased_random(132, 252, 318, 56)
    delay = biased_random(19394, 189780, 518400, 79230)
    values[n]['parts oreder'] = round(determine+order+delay, 2)
