dwords = {}
dwords_eng_ru = {}
dwords_de_eng = {}
# add repeating checking in words
# checking blank lines
d = {

    'Nacht': 'Ночь',
    'Auto': 'Авто',
    'Schnee': 'Снег',
    'Wärme': 'Тепло',
    'Sonne': 'Солнце',
    'Stern': 'Звезда',
    'Mond': 'Луна',
    'Mütze': 'Шапка',
    'Mensch': 'Человек',
    'Zelt': 'Шалаш',

}

with open("DEtoRU.txt") as file:
    for line in file:
        if line[0] != '#':
            key, *value = line.split()
            dwords[key] = str(value[0])

dwords_reverse = ({v: k for k, v in dwords.items()})

with open("ENGtoRU.txt") as file:
    for line in file:
        if line[0] != '#':
            key, *value = line.split(sep='-')
            value[0] = str(value[0]).replace('\n', '')
            dwords_eng_ru[key] = str(value[0])

dwords_eng_ru_reverse = ({v: k for k, v in dwords_eng_ru.items()})

i = 0
with open("DEtoENG.txt") as file:
    for line in file:
        if line[0] != '#':
            #print(line.split())
            #print(i)
            i = i + 1
            key, *value = line.split()
            dwords_de_eng[key] = str(value[0])


dwords_de_eng_reverse = ({v: k for k, v in dwords_de_eng.items()})
