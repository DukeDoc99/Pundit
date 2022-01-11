import sympy as sym

def printout(solution, variables, fp=False):
    for var in variables:
        sym.pretty_print(var)
        if fp:
            sym.pretty_print(solution[var].evalf(fp))
        else:
            sym.pretty_print(solution[var])
    print()
    
def makesubs(solution, vartosub, valtosub):
    subsol = solution.copy()
    sublist = list(zip(vartosub, valtosub))
    for var in solution:
        subsol[var] = subsol[var].subs(sublist)
    return subsol