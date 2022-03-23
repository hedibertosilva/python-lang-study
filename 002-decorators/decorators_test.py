#!/usr/bin/env python3
"""
    Based on Anthony Explains
    https://www.youtube.com/watch?v=sv46294LoP8&list=PLWBKAf81pmOaP9naRiNAqug6EBnkPakvY&index=2
"""
import decorators


def test_normal_decoration():
    """ Testing normal decoration. """
    @decorators.dec
    def g(x: int) -> int:
        return f'g({x})'

    assert g(0) == "g(0) + C"


def test_decoration_with_params(capsys):
    """ Testing decoration with extra parameters. """
    @decorators.dec_aux("Hello", "Good Bye")
    def h(x: int) -> int:
        return f'h({x})'

    h(0)

    out, err = capsys.readouterr()
    assert out == "gretting => Hello\nfarewell => Good Bye\n"
    assert err == ""
