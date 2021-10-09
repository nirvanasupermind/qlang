from symbol_table import SymbolTable
from values import *

def func_I(args):
    return String(input())

def func_P(args):
    print(args[0])
    return At()

stdlib = SymbolTable()
stdlib.set('P', Func(func_P))