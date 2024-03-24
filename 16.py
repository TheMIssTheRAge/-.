# Колесо фортуны.
import random
from time import*

def ran():
    name = random.choice(spic)
    print("И побеждает...")
    sleep(2)
    print(f"Выигрывает: {name}")

spic = [] 

dob = input("Добавить участника?: ")
if dob == "да":
    lud = input("Участник: ")
    spic.append(lud)


while dob != "нет":
    dob = input("Добавить участника?: ")
    if dob == "да":
        lud = input("Участник: ")
        spic.append(lud)

ran()




