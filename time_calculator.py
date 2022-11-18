days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def add_time(start, duration, display_day=None):
    if display_day == None:
        current_day = 0
    else:
        display_day = display_day.capitalize()
        current_day = days.index(display_day)   

    start = start.split(':')
    hr = start[0]
    time_suffix = start[1].split()
    mins = time_suffix[0]
    am_pm = time_suffix[1]
    n_days = 0

    duration = duration.split(':')
    duration_hr = duration[0]
    duration_mins = duration[1]
            
    new_hr = int(hr) + int(duration_hr)
    new_mins = int(mins) + int(duration_mins)

    while new_mins > 59:
        new_mins -= 60
        new_hr += 1

    while new_hr > 11:
        new_hr -= 12
        if am_pm == 'AM':
            am_pm = 'PM'
        elif am_pm == 'PM':
            am_pm = 'AM'
            if current_day == 6:
                current_day = 0
            else:
                current_day += 1
            n_days += 1
    
    if new_mins < 10:
        new_mins = '0' + str(new_mins)
    
    if new_hr == 0:
        new_hr = 12
    
    new_hr = str(new_hr)
    new_mins = str(new_mins)

    if not n_days:
        str_n_days = ''
    if n_days == 1:
        str_n_days = ' (next day)'
    elif n_days > 1:
        str_n_days = f' ({n_days} days later)'
    
    if display_day == None:
        new_time = f'{new_hr}:{new_mins} {am_pm}{str_n_days}'
    else:
        new_time = f'{new_hr}:{new_mins} {am_pm}, {days[current_day]}{str_n_days}'
    return new_time