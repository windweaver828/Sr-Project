def charge(seconds, rate):
    cost = seconds / 3600
    cost = cost * rate
    return round(cost,2)
