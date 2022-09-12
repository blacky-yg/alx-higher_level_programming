#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0
    for i in range(1, 3):
        try:
            if i <= a:
                res += a ** b / i
            else:
                raise Exception('Too far')
        except Exception:
            res = b + a
            break
    return res
