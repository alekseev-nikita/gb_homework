def refactor_digit(element):
    start, end, mid = '', '', ''
    for ch in element:
        if ch.isdigit():
            mid += ch
        elif mid:
            end += ch
        else:
            start += ch
    mid = int(mid)
    return f'{start}{mid:02d}{end}'


msg = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for idx in range(len(msg)-1, -1, -1):
    value = msg.pop(idx)
    if any(ch.isdigit() for ch in value):
        msg.insert(idx, '"')
        msg.insert(idx, refactor_digit(value))
        msg.insert(idx, '"')
    else:
        msg.insert(idx, value)

line = ' '.join(msg)
print(msg)

new_line = ''
trim_right = True
ignore = 0
for idx, value in enumerate(line):
    if value != ' ':
        new_line += value
    else:
        if trim_right:
            if line[idx - 1] == '"' and ignore != idx - 1:
                trim_right = False
                continue
            else:
                new_line += value
        elif not trim_right:
            if line[idx + 1] == '"':
                trim_right = True
                ignore = idx + 1
                continue
            else:
                new_line += value
print(new_line)

