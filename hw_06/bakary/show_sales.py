import sys


def show(_, *args):
    start = int(args[0])-1 if len(args) == 1 else 0
    end = int(args[1]) if len(args) == 2 else -1
    with open('bakery.csv', 'r', encoding='UTF-8') as f:
        for idx, line in enumerate(f):
            if end != -1 and idx > end:
                break
            if idx < start:
                continue
            if idx >= start and (end == -1 or idx < end):
                print(line.rstrip())


if __name__ == '__main__':
    show(*sys.argv)
