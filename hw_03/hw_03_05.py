#Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
#Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?
from random import randrange


def get_jokes(jokes_num, is_unique=False):
    jokes = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for i in range(0, jokes_num):
        noun = nouns.pop(randrange(0, len(nouns))) if is_unique else nouns[randrange(0, len(nouns))]
        adverb = adverbs.pop(randrange(0, len(adverbs))) if is_unique else adverbs[randrange(0, len(adverbs))]
        adjective = adjectives.pop(randrange(0, len(adjectives))) if is_unique else adjectives[randrange(0, len(adjectives))]
        jokes.append(' '.join([noun, adverb, adjective]))
    print(jokes)


get_jokes(1)
get_jokes(2)
get_jokes(3, is_unique=True)
