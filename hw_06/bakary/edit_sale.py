import sys


def get_data():
    with open('bakery.csv', 'r', encoding='UTF-8') as f:
        for idx, line in enumerate(f):
            yield idx+1, line


def edit(line_num, price):
    line_num = int(line_num)
    price = price.replace('.', ',') + '\n'
    data = dict(get_data())
    if data.get(line_num) is None:
        print('Line number out of limit')
    data[line_num] = price
    print(data)
    prices = (p for p in data.values())
    with open('bakery.csv', 'w', encoding='UTF-8') as f:
        while True:
            try:
                f.write(next(prices))
            except StopIteration:
                break


if __name__ == '__main__':
    edit(*sys.argv)
