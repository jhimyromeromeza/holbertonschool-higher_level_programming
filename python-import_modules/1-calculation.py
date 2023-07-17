#!/usr/bin/python3
if __name__ == "__main__":
    
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    resultado_add = add(a, b)
    resultado_sub = sub(a, b)
    resultado_mul = mul(a, b)
    resultado_div = div(a, b)
    print("{} + {} = {}".format(a, b, resultado_add))
    print("{} - {} = {}".format(a, b, resultado_sub))
    print("{} * {} = {}".format(a, b, resultado_mul))
    print("{} / {} = {}".format(a, b, resultado_div))
