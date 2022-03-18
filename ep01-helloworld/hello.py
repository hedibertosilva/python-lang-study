#!/usr/bin/env python3
"""
    Antony Explains
    https://www.youtube.com/watch?v=sv46294LoP8&list=PLWBKAf81pmOaP9naRiNAqug6EBnkPakvY&index=2
"""
import argparse
import sys
from typing import Optional
from typing import Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    """ Initializer. """
    parser = argparse.ArgumentParser()
    parser.add_argument('person')
    args = parser.parse_args(argv)

    if args.person == '':
        print("Person's name must no be empty!", file=sys.stderr)
        return 1

    print(f"Hello {args.person}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
