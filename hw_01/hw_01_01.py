def show_real_time(duration):
    time_stemp = {
        'дн': 86400,
        'час': 3600,
        'мин': 60,
        'сек': 1
    }
    result = ''
    for key, value in time_stemp.items():
        step = duration // value
        duration %= value
        if step != 0:
            result += f'{step} {key} '
    print(result)


show_real_time(400153)
