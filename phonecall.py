from random import gauss, randint


def biased_random(minimum, mean, maximum, stdev):
    value = gauss(mean, stdev)
    if '-' in str(value):
        value = gauss(mean, stdev)
    else:
        return value

def phone(n, values):
    values[n]['call time'] = round(float(biased_random(0, 762, 2724, 333)), 2)
    values[n]['call duration'] = round(float(biased_random(45, 216, 738, 79)), 2)
    return values
