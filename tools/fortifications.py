#!/usr/bin/env python3
import ast
import os
import sys


def iter_python(paths):
    for path in paths:
        if os.path.isfile(path) and path.endswith('.py'):
            yield path
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for name in files:
                    if name.endswith('.py'):
                        yield os.path.join(root, name)


def main(paths):
    bad = []
    for path in iter_python(paths):
        with open(path, 'r', encoding='utf-8') as handle:
            tree = ast.parse(handle.read(), filename=path)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'eval':
                bad.append('%s:%s eval() call' % (path, node.lineno))
    if bad:
        print('\n'.join(bad), file=sys.stderr)
        return 1
    print('fortifications ok')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
