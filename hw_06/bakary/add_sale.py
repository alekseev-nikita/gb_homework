import sys


def add(price):
    try:
        float(price.replace(',', '.'))
    except ValueError:
        print(f'Invalid value: {price}')
        return
    with open('bakery.csv', 'a', encoding='UTF-8') as f:
        f.write(price.replace('.', ',') + '\n')


if __name__ == '__main__':
    add(sys.argv[1])
