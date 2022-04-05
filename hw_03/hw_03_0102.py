# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
# Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
def num_translate_adv(en_num: str):
    num_dict = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    return num_dict.get(en_num.lower()) if en_num.islower() else num_dict.get(en_num.lower()).capitalize()


en_nums = ('One', 'two', 'three', 'Four', 'Five', 'Six', 'seven', 'eight', 'Nine', 'ten', 'eleven')
ru_nums = tuple(map(num_translate_adv, en_nums))
print(ru_nums)
