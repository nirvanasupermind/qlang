from symbol_table import SymbolTable
from values import *

def func_I(args):
    return String(input())

def func_N(args):
    if isinstance(args[0], Number):
        return args[0]
    elif isinstance(args[0], String):
        try:
            return Number(float(args[0]))
        except ValueError:
            return At()
    else:
        return At()

def func_P(args):
    print(args[0])
    return At()

def func_S(args):
    return String(str(args[0]))

stdlib = SymbolTable()
stdlib.set('I', Func(func_I))
stdlib.set('N', Func(func_N))
stdlib.set('P', Func(func_P))
stdlib.set('S', Func(func_S))