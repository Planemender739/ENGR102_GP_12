am_pm_block = None
if '12' in clock_type:
    if hour == 0:
        hour = 12
        am_pm_block = DIGITS['AM']
    elif hour == 12:
        am_pm_block = DIGITS['PM']
    elif hour > 12:
        hour -= 12
        am_pm_block = DIGITS['PM']
    else:
        am_pm_block = DIGITS['AM']

hour_str = str(hour)
adjusted_time = hour_str + ":" + minutes
