import operator


def parse_expr(info):
    n1, sign, n2 = info.split()
    op = {
        '/': operator.truediv,
        '*': operator.mul,
        '+': operator.add,
        '-': operator.sub,
        '^': operator.pow
    }[sign]
    return op, float(n1), int(n2)