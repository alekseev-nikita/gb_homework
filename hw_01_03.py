def declension(num):
    num = str(num)
    if num.endswith(('5', '6', '7', '8', '9', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20')):
        print(f'{num} процентов')
    elif num.endswith('1'):
        print(f'{num} процент')
    elif num.endswith(('2', '3', '4')):
        print(f'{num} процента')


for i in range(1, 101):
    declension(i)
