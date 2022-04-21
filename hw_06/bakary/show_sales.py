import sys


def show(start=0, end=-1):
    start = int(start)
    end = int(end)
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
