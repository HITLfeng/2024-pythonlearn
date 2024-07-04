
class BaseAttr:
    def __init__(self, blood, attackCnt, attack, defense):
        self.blood = blood
        self.attackCnt = attackCnt
        self.attack = attack
        self.defense = defense



class Plant(BaseAttr):
    pass


class Zombie(BaseAttr):
    pass