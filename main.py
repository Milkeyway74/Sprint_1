import datetime as dt
import decimal as dc

FORMAT = '%H:%M:%S'
WEIGHT = 75
HEIGHT = 175
K_1 = 0.035
K_2 = 0.029
STEP_M = 0.65

storage_data = {}
def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    if len(data) != 2 or None in data:
        return False
    else:
        return True

def check_correct_time(data):
    """Проверка корректности параметра времени."""
    time, steps = data
    if len(storage_data) != 0 and time >= max(storage_data.keys()):
        return False
    else:
        return True

def get_step_day(steps):
    result = sum(storage_data.values()) + steps
    #for i in storage_data.values():
        #result += i
    return result

def get_distance(steps):
    dist = get_step_day(steps) * STEP_M/1000
    return dist

def get_spent_calories(dist, time):
    #dist = get_distance(steps)
    current_time = dt.datetime.strptime(time, FORMAT).time()
    time = dc.Decimal(current_time.hour) + dc.Decimal(current_time.minute)/60
    ms = dc.Decimal(dist) / dc.Decimal(time)
    spent_calories = ((K_1 * WEIGHT + (dc.Decimal(ms))**2 / HEIGHT) * K_2 *WEIGHT) * time*60
    return spent_calories

def get_achievement(dist):
    """Получить поздравления за пройденную дистанцию."""
    if dist >= 6.5:
        achievement = 'Отличный результат! Цель достигнута.'

    elif dist >= 3.9:
        achievement = 'Неплохо! День был продуктивным.'
    elif dist >= 2:
        achievement = 'Маловато, но завтра наверстаем!'
    else:
        achievement = 'Лежать тоже полезно. Главное — участие, а не победа!'
    return achievement


def show_message(time, steps, dist, spent_calories, achievement):
    print(f'''


    Время: {time}.
    Количество шагов за сегодня: {steps}.
    Дистанция составила {dist} км.
    Вы сожгли {spent_calories} ккал.
    {achievement}''')


def accept_package(data):
    # """Обработать пакет данных."""
    if check_correct_data(data) == False:  # Если функция проверки пакета вернет False
        return 'Некорректный пакет'
    # Распакуйте полученные данные.
    time, steps = data
    pack_time = dt.datetime.strptime(time, FORMAT)  # Преобразуйте строку с временем в объект типа time.
    if check_correct_time(data) == False:  # Если функция проверки значения времени вернет False
        return 'Некорректное значение времени'
    else:

        time, steps = data
        storage_data[time] = steps
    day_steps = get_step_day(steps)  # Запишите результат подсчёта пройденных шагов.
    dist = get_distance(steps)  # Запишите результат расчёта пройденной дистанции.
    spent_calories = get_spent_calories(dist, time)  # Запишите результат расчёта сожжённых калорий.
    achievement = get_achievement(dist)  # Запишите выбранное мотивирующее сообщение.
    return show_message(time, steps, dist, spent_calories, achievement)

package_0 = ('2:00:01', 505)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)
