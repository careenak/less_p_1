x = float(input("Введите выручку фирмы "))
y = float(input("Введите издержки фирмы "))
if x > y:
    print(f"Фирма работает с прибылью. Прибыль составляет {x - y}. Рентабельность выручки составила {y / x:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {(x - y) / workers:.2f}")
elif x == y:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")