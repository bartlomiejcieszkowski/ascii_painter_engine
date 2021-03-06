#!/usr/bin/env python3


import argparse
import os.path
import pkgutil
import tests
import importlib
import sys

import log

def main():
    tests_path = os.path.dirname(tests.__file__)
    tests_list = [name for _, name, _ in pkgutil.iter_modules([tests_path])]
    print(tests_list)
    parser = argparse.ArgumentParser(description='Run tests.')
    parser.add_argument('--test', '-t', choices=tests_list, required=True)
    args = parser.parse_args()

    print(args.test)
    sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir, '..')))
    x = importlib.import_module(f'tests.{args.test}')

    log.log_file(f'{args.test}')
    x.test()
    sys.exit(0)


if __name__ == '__main__':
    main()
