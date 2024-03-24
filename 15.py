def new():
    spr = input("Добавить магазин?: ")
    if spr == "да":
     dobav = input("Магазин: ")
     tov = int(input("Сколько товаров: "))
     status = input("Каков статус магазина: ")
     spic[dobav] = f"Товаров: {tov} / Статус: {status}"

    while spr != "нет":
       spr = input("Добавить магазин?: ")
       if spr == "да":
        dobav = input("Магазин: ")
        tov = int(input("Сколько товаров: "))
        status = input("Каков статус магазин: ")
        spic[dobav] = f"Товаров: {tov} / Статус: {status}"

def delet():
  v = input("Удалить магазин?: ")
  if v == "да":
    v1 = input("Какой магазин удалить?: ")
    del spic[v1]
  else:
    print("Хорошо")
        

spic = {}

new()
for key, values in spic.items():
  print(f"{key} - {values}")

delet()

new()
for key, values in spic.items():
  print(f"{key} - {values}")




