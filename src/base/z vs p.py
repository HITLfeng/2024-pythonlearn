import os
import random
import time


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


def showImage(lstPlant, lstZombie):
    print("##########################################")
    print("\n")
    for plant in lstPlant:
        print(plant.blood, end=' ')
    print("\n")
    for zombie in lstZombie:
        print(zombie.blood, end=' ')
    print("\n")


def chcekBlood(lst):
    for item in lst:
        if item.blood > 0:
            return True
    return False


def gameFinish(lstPlant, lstZombie):
    return chcekBlood(lstPlant) and chcekBlood(lstZombie)


def plantAttack(lstPlant, lstZombie):
    for plant in lstPlant:
        if plant.blood <= 0:
            continue
        if chcekBlood(lstZombie) == False:
            return
        while True:
            zombie = random.choice(lstZombie)
            if zombie.blood > 0:
                break
        print(
            f"植物(攻击力{plant.attack} 攻击次数{plant.attackCnt})对僵尸(防御 {zombie.defense})攻击了多次，造成伤害{(plant.attack - zombie.defense) * plant.attackCnt}")
        zombie.blood -= (plant.attack - zombie.defense) * plant.attackCnt
        if zombie.blood < 0:
            zombie.blood = 0
    print("##########################################")


def zombieAttack(lstPlant, lstZombie):
    for zombie in lstZombie:
        if zombie.blood <= 0:
            continue
        if chcekBlood(lstPlant) == False:
            return
        while True:
            plant = random.choice(lstPlant)
            if plant.blood > 0:
                break
        print(
            f"僵尸(攻击力{zombie.attack} 攻击次数{zombie.attackCnt})对植物(防御 {zombie.defense})攻击了多次，造成伤害{(zombie.attack - plant.defense) * zombie.attackCnt}")
        plant.blood -= (zombie.attack - plant.defense) * zombie.attackCnt
        if plant.blood < 0:
            plant.blood = 0
    print("##########################################")

def gameStart(lstPlant, lstZombie):
    while gameFinish(lstPlant, lstZombie):
        showImage(lstPlant, lstZombie)
        plantAttack(lstPlant, lstZombie)
        showImage(lstPlant, lstZombie)
        if chcekBlood(lstZombie) == False:
            print("植物获胜！")
            break
        time.sleep(3)
        zombieAttack(lstPlant, lstZombie)
        showImage(lstPlant, lstZombie)
        if chcekBlood(lstPlant) == False:
            print("僵尸获胜！")
            break
        time.sleep(3)

        os.system('cls')
        # print("\033c", end="")


def heroPrepare(lstPlant, lstZombie):
    plantCnt = random.randint(10, 12)
    for i in range(plantCnt):
        lstPlant.append(
            Plant(random.randint(400, 500), random.randint(5, 9), random.randint(80, 120), random.randint(1, 10)))
    zombieCnt = random.randint(12, 16)
    for i in range(zombieCnt):
        lstZombie.append(
            Zombie(random.randint(1500, 2800), random.randint(1, 2), random.randint(45, 99), random.randint(10, 20)))


if __name__ == '__main__':
    # 初始化双方阵容
    # 每方 4-6 名英雄
    lstPlant = []
    lstZombie = []
    heroPrepare(lstPlant, lstZombie)
    gameStart(lstPlant, lstZombie)
