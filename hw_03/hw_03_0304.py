# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
# в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы
from collections import OrderedDict


def thesaurus_adv(*args):
    ppl = {}
    for arg in args:
        name, surname = arg.split()
        if ppl.get(surname[0]) is None:
            ppl[surname[0]] = {name[0]: [arg]}
        else:
            if ppl.get(surname[0]).get(name[0]) is None:
                ppl[surname[0]][name[0]] = [arg]
            else:
                t_list = ppl.get(surname[0]).get(name[0])
                t_list.append(arg)

    return ppl


ppl_adv = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(ppl_adv)
print(dict(OrderedDict(sorted(ppl_adv.items()))))
