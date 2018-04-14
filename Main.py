#!/usr/bin/env python
# Created by James Upton

"""Usage:
    simulate
    simulate (-h | --help)
    simulate (-v | --version)

Options:
    -h, --help          show this help message and exit
    -v, --version       show program's version number and exit
"""

import os
import sys
from keith import Process
import generatejob

Process.chgProcessName('simulate')
n=1

def main(n):    
    while n < 1000:
        jobs = generatejob.job()
        n+=1
        for k, v in jobs.iteritems():
            print(v)
        
if __name__ == '__main__':    
    main(n)
    
