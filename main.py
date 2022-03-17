import random

bandas_rock = {'queen': ['Radio Gaga', 'the show must go on', 'dust'], 'system of a down': ['byob', 'aerials'],
               'iron maiden': ['fear of the dark', 'the number of the beast', 'run to the hills',
                               'alexander the great']}

secreto = random.choice(list(bandas_rock))
print(secreto)
musicas = bandas_rock[secreto]
print(musicas)