class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power

    def tibbers(self):
        print('티버: 피해량 {0}'.format(400 + 0.65 * self.ability_power))
    #    print(400 + 0.65 * self.ability_power)

health, mana, ability_power = map(float, input().split())

x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()
