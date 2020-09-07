def prod_replicate(x, repeat):
    result = [[]]
    replicate = [x] * repeat
    for rep in replicate:
        result = [i + [j] for i in result for j in rep]
    return result

def expr(p):
    return "{}1{}2{}3{}4{}5{}6{}7{}8{}9".format(*p)

def gen_expr():
    op = ['+', '-', '']
    #print([expr(p) for p in product(op, repeat=9) if p[0] != '+'])
    #return [expr(p) for p in product(op, repeat=9) if p[0] != '+']
    result = []
    for p in prod_replicate(op, repeat=9):
        if p[0] != "+":
            result.append(expr(p))
    return result

def all_exprs():
    values = {}
    for expr in gen_expr():
        val = eval(expr)
        if val not in values:
            values[val] = 1
        else:
            values[val] += 1
    return values

def sum_to(val):
    for s in filter(lambda x: x[0] == val, map(lambda x: (eval(x), x), gen_expr())):
        print(s)

sum_to(100)
