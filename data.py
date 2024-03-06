from datetime import date
# Читаем данные об ученых
data = open("scientist.txt", encoding='utf-8').read().strip().split('\n')[1:]

data = list(map(lambda s: s.split('#'), data))

NAME='name'
PREP='prep'
DATE='date'
COMP='comp'

# Приводим в нормальный вид
data = list(map(lambda d: {
    NAME: d[0],
    PREP: d[1],
    DATE: date.fromisoformat(d[2]),
    COMP: d[3].split(' ')
}, data))

DATA = data

preps = {}
allo_origin = None
allo_fakers = []
data.sort(key=lambda r: r[DATE])
for r in data:
    if r[PREP] not in preps:
        if r[PREP] == "Аллопуринол":
            allo_origin = r
        preps[r[PREP]] = r
    elif r[PREP] == "Аллопуринол":
        allo_fakers.append(r)


preps = list(preps.values())
preps.sort(key=lambda i: i[DATE])