from itertools import zip_longest


def get_tutors_with_klasses():
    tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Ильдар']
    klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
    for tutor, klass in zip_longest(tutors, klasses, fillvalue=None):
        yield tutor, klass


tutors_data = get_tutors_with_klasses()
for _ in range(9):
    print(next(tutors_data))
