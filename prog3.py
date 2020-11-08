prod = {'S1222': 'sukienka trojkatna',
            'P1222': 'koszulka',
            'X212': 'konsola do gier'}

igla = 'P12'

if igla in prod:
    print('istnieje')
else:
    print(prod['P1222'])


produkty = {'SS12': {'nazwa': 'sukienka trojkatna', 'rozmiary': ['s','l','xl']},
            'P12': {'nazwa': 'spodnica','rozmiary': ['s', 'xl']}
            }

for id in produkty:
    p = produkty[id]
    rozmiary = p['rozmiary']
    print(p['nazwa'])
    for r in rozmiary:
        print(r)
