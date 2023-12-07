points = {'Иванов': 20, 'Сидоров': 68, 'Петров': 28, 'Смирнов': 68}

points['Кондратьев'] = -100
points['Мясников'] = 100
points['Косточкин'] = 65

min_points = min(points.values())
name_min_points = 0
for x in points:
    if points.get(x) == min_points:
        name_min_points = x

max_points = max(points.values())
name_max_points = 0
for x in points:
    if points.get(x) == max_points:
        name_max_points = x

mid_points = sum(points.values()) / len(points)
best_rez = []
for x in points:
    if points.get(x) > mid_points:
        best_rez.append(x)

print(f'Минимальный результат {min_points} - {name_min_points}')
print(f'Наилучший результат {max_points} - {name_max_points}')
print("Средний балл: ", '%.2f' % mid_points)
print("Участники у кого балл выше среднего: ", *sorted(best_rez))
