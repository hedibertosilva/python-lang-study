#!/usr/bin/env python3
"""
    Based on Anthony Explains
    https://www.youtube.com/watch?v=sv46294LoP8&list=PLWBKAf81pmOaP9naRiNAqug6EBnkPakvY&index=2
"""
import hello


def test_main(capsys):
    """ Testing normal expect input. """
    hello.main(['Hediberto'])

    out, err = capsys.readouterr()
    assert out == 'Hello Hediberto\n'
    assert err == ''


def test_main_error_with_empty_string(capsys):
    """ Testing expect output when we populate with empty string. """
    hello.main([''])

    out, err = capsys.readouterr()
    assert out == ''
    assert err == "Person's name must no be empty!\n"
