#!/usr/bin/env python3
"""
    Based on Anthony Explains
    https://www.youtube.com/watch?v=WDMr6WolKUM&list=PLWBKAf81pmOaP9naRiNAqug6EBnkPakvY&index=3
"""
import functools


def dec(func):
    """ Normal decoration. """
    @functools.wraps(func) # to preserve proprieties
    def dec_inner(*args, **kwargs):
        res = func(*args, **kwargs) + ' + C'
        return res
    return dec_inner

def dec_aux(gretting, farewell):
    """ Testing decoration with extra parameters. """
    def dec_aux_decorator(func):
        @functools.wraps(func) # to preserve proprieties
        def dec_aux_inner(*args, **kwargs):
            print('gretting =>', gretting)
            res = func(*args, **kwargs)
            print('farewell =>', farewell)
            return res
        return dec_aux_inner
    return dec_aux_decorator

@dec_aux("Hi", "Bye")
def f(x: int) -> str:
    return f'f({x})'

def main():
    print(f(0))


if __name__ == '__main__':
    raise SystemExit(main())
