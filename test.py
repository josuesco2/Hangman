#!/usr/bin/env python

def counter():
    count = 5
    while count > 0:
        yield count
        count = count - 1

clone = counter()
try:
    while True:
        print clone.next()
except StopIteration:
    print "we hit the end"
