import os
import sys
from random import gauss, randint
import buffing
import cleanup
import delivery
import estimate
import graph
import paint
import phonecall
import prep

n=1
paintlist = []
if __name__ == '__main__':
    while n < 11:
        values = {}
        values[n] = {}
        call_time = phonecall.phone(n, values)
        estimate_time = estimate.gen_estimate(n, values)
        prep_time = prep.prepare(n, values)
        paint_time = paint.deliver(n, values)
        delivery_time = delivery.deliver(n, values)
        buff_time = buffing.buff(n, values)
        clean_up = cleanup.port(n, values)
        for k,v in values[n].items():
            if k == 'prep time':
                paintlist.append(v/60)
##                paintlist.append(0)
        n+=1
        print values
    graph.plot(sorted(paintlist))
##    ['estimate details']

