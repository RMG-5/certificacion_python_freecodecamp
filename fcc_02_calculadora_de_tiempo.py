'''Calculadora de Tiempo'''


def add_time(start, duration, weekday=None):
    '''Función para calcular el tiempo transcurrido'''

    weekdays = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Calcula la hora de inicio en minutos (empezando a las 12:00 AM)
    if start.split()[1] == 'PM':
        time_initial = 720 + \
            int(start.split(':')[0]) * 60 + int(start.split(':')[1].split()[0])
    else:
        time_initial = int(start.split(
            ':')[0]) * 60 + int(start.split(':')[1].split()[0])

    # Calcula la duracion en minutos
    time_duration = int(duration.split(
        ':')[0]) * 60 + int(duration.split(':')[1])

    # Calcula el tiempo final en minutos (empezando a las 12:00 AM) de la hora de inicio
    time_total = int(time_initial + time_duration)

    # Calcula la hora final cuando NO se encuentra dentro del dia de inicio
    if time_total >= 1440:
        if int(time_total % 1440) > 720:
            hour_finish = int((time_total % 1440 - 720) / 60)
            period_finish = 'PM'
        else:
            hour_finish = int((time_total % 1440) / 60)
            period_finish = 'AM'

        # Calcula los dias transcurridos
        if int(time_total / 1440) == 1:
            days_passed = '(next day)'
        else:
            days_passed = f'({int(time_total / 1440)} days later)'

    # Calcula la hora final cuando SI se encuentra dentro del dia de inicio
    if time_total < 1440:
        days_passed = ''
        if time_total > 720:
            hour_finish = int((time_total - 720) / 60)
            period_finish = 'PM'
        else:
            hour_finish = int(time_total / 60)
            period_finish = 'AM'

    # Calcula el minuto final
    minute_finish = int(time_total % 60)

    # Calcula el numero de dia de la semana del tiempo final
    if weekday:
        number_day = (weekdays.index(weekday.capitalize()) +
                      int(time_total / 1440)) % len(weekdays)

    # Devuelve el tiempo final en el formato solicitado
    return f"{12 if hour_finish == 0 else hour_finish}:{str(minute_finish).zfill(2)}\
 {period_finish}{', ' + weekdays[number_day] if weekday else ''} {days_passed}".strip()


# ********** ********** ********** ********** ********** ********** ********** #
# Ejemplo de uso #

print(add_time('3:30 PM', '2:12'))
print(add_time('11:55 AM', '3:12'))
print(add_time('2:59 AM', '24:00'))
print(add_time('11:59 PM', '24:05'))
print(add_time('8:16 PM', '466:02'))
print(add_time('3:30 PM', '2:12', 'Monday'))
print(add_time('2:59 AM', '24:00', 'saturDay'))
print(add_time('11:59 PM', '24:05', 'Wednesday'))
print(add_time('8:16 PM', '466:02', 'tuesday'))

# ********** ********** ********** ********** ********** ********** ********** #
