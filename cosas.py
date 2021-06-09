class Personaje:
    hp = 100
    resistencia = 20
    xp = 3
    vidas = 4
    def gameOver(self):
        print ('Game over')


class per():
    """docstring for per."""

    def __init__(self, hp, resistencia,xp,vidas):
        self.hp = hp
        self.resistencia = resistencia
        self.xp = xp
        self.vidas = vidas

# ninja = Personaje()

# print(ninja.gameOver)

ninja = per(50,20,3,5)
ninja.correr = 90
print(ninja.correr)
