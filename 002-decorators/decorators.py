#!/usr/bin/env python3
"""
    Based on Anthony Explains
    https://www.youtube.com/watch?v=WDMr6WolKUM&list=PLWBKAf81pmOaP9naRiNAqug6EBnkPakvY&index=3
"""
import functools
from typing import Any
from typing import Callable


def dec(func: Callable) -> Callable:
    @functools.wraps(func)
    def dec_inner(*args: tuple, **kwargs: dict) -> str:
        res = func(*args, **kwargs) + ' + C'
        return res
    return dec_inner

def dec_aux(gretting: Any, farewell: Any) -> Callable:
    """ Testing the decorator with extra parameters.
        Basically it's a normal decorator wrapped.

    Args:
        gretting (Any): initial information.
        farewell (Any): final information.

    Returns:
        Callable: it returns the decorator function.
    """
    def dec_aux_decorator(func: Callable) -> Callable:
        """ It's responsible for receive original function, make something,
            and returns the inner function.

            Args:
                func (Callable): the original function.

            Returns:
                Callable: the inner function.
        """
        @functools.wraps(func) # The functools.wraps preserve the initial props.
        def dec_aux_inner(*args: tuple, **kwargs: dict) -> Any:
            """ It's responsible for receive the input parameters to the original
                function, make something with them, and return the results from original function.

                Args:
                    args (tuple)
                    kwargs (dict)

                Returns:
                    Any: original function output.
            """
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
