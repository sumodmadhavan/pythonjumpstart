__author__ = 'ravi'

import fileinput

for line in fileinput.input():
    print "{:>6}  {}".format(fileinput.lineno(), line.rstrip())
