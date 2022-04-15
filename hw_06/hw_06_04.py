def get_data(file_name):
    with open(file_name, 'r', encoding='UTF-8') as f:
        for line in f:
            yield line.rstrip()


def write_data_to_file():
    users = get_data('users.csv')
    hobbies = get_data('hobby.csv')
    with open('users_data.txt', 'w', encoding='UTF-8') as f:
        while True:
            try:
                user = next(users)
            except StopIteration:
                user = None
            try:
                hobby = next(hobbies)
            except StopIteration:
                hobby = None
            if hobby and user is None:
                raise StopIteration
            elif user is None and hobby is None:
                break
            f.write(f'{user}: {hobby}\n')


write_data_to_file()
