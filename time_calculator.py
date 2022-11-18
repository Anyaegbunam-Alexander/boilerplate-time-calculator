days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def add_time(start, duration, o_day=None):
    if o_day == None:
        day = 0
    else:
        o_day = o_day.capitalize()
        day = days.index(o_day)   

    start = start.split(':')
    hr = start[0]
    m_am = start[1].split()
    mins = m_am[0]
    am_pm = m_am[1]
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
            if day == 6:
                day = 0
            else:
                day += 1
            n_days += 1
    
    if new_mins < 10:
        new_mins = '0' + str(new_mins)
    
    if new_hr == 0:
        new_hr = 12
    
    new_hr = str(new_hr)
    new_mins = str(new_mins)

    if not n_days:
        str_days = ''
    if n_days == 1:
        str_days = ' (next day)'
    elif n_days > 1:
        str_days = f' ({n_days} days later)'
    
    if o_day == None:
        new_time = f'{new_hr}:{new_mins} {am_pm}{str_days}'
    else:
        new_time = f'{new_hr}:{new_mins} {am_pm}, {days[day]}{str_days}'
    return new_time