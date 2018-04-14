from random import gauss, randint
import prep



def biased_random(minimum, mean, maximum, stdev):
    value = gauss(mean, stdev)
    if minimum < value < maximum:
        return value
    else: value = gauss(mean, stdev)
    return value

def gen_estimate(n, values):
    values[n] = {}
    values[n]['estimate time'] = round(biased_random(4800, 5760, 7200, 446), 2)
    values[n]['estimate duration'] = round(write_estimate(), 2)
    values[n]['estimate details'] = {}
    estimate_details(n, values)
    return values

def estimate_details(n, values):
    body_time = biased_random(0, 12.6, 65.6, 6.39)
    body_scale = (body_time / 12.6)
    if body_time < 5:
        paint_time = biased_random(0, 7.92, 22.7, 3.69)
    else:
        paint_time = body_time * biased_random(0.35, 0.63, 0.86, 0.13)    
    paint_scale = (paint_time / 7.92)
    parts_cost = round(body_time * biased_random(.65, 1.02, 14, 0.17)*100, 2)
    if body_time > 0 and paint_time > 0 and parts_cost > 0:
        values[n]['estimate details']['body'] = round(body_time, 2)
        values[n]['estimate details']['paint'] = round(paint_time, 2)
        values[n]['estimate details']['parts'] = parts_cost
        values[n]['estimate details']['paintscale'] = round(paint_scale, 2)
        values[n]['estimate details']['bodyscale'] = round(body_scale, 2)
    else:
        estimate_details(n, values)
    return values
        
def write_estimate():
    gather = biased_random(45, 90, 120, 21) 
    picture = biased_random(0, 260, 492, 121)
    data_input = biased_random(37, 130, 398, 43)
    explain = biased_random(18, 69, 332, 24)
    time = gather+picture+data_input+explain
    return time
