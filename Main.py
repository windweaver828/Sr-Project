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

# import docopt for the above cmdline functionality to work
from keith import Process
import generatejob

Process.chgProcessName('simulate')


def main():
    for _ in xrange(1, 1000)
        for job in generatejob.job().values():
            print(job)

if __name__ == '__main__':    
    main()
