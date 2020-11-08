game = {'hit': -10,
        'kick': -15,
        'shoot': -20,
        'bomb': -25}

user_hp = 100

def loose_life(play):
    attack = sum(game.values())
    result = user_hp + attack
    return result

what_is_left = loose_life(game)
print(what_is_left)


app = {'user_name': 'Anna',
        'user_age': 23,
        'user_hight': 1.68}

print(app['user_name'])


for klucz in app:
    print(app[klucz])

app['user_eye_color'] = 'blue'

for klucz in app:
    print("{0}: {1}".format(klucz,app[klucz]))

for key, value in app.items():
    print("{0}: {1}".format(key, value))
