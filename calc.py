#!/usr/bin/python
def sqroot(a, digits):
    a = a * (10**(2*digits))
    x_prev = 0
    x_next = 1 * (10**digits)
    while x_prev != x_next:
        x_prev = x_next
        x_next = (x_prev + (a // x_prev)) >> 1
    return x_next
print sqroot(2, 1000000)
