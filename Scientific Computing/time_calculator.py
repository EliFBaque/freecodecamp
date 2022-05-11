def add_time(starting_time, addition_time, day=False):
    array_start = starting_time.split()  
    array_add = addition_time.split() 

    hour_mode = array_start[1]
    start = array_start[0].split(':') 
    addition = array_add[0].split(':')  
    
    hours_start = int(start[0])  
    minutes_start = int(start[1])  
    hours_add = int(addition[0]) 
    minutes_add = int(addition[1])  
    day_count = 0
    # Addition of minutes and extra hours
    if(minutes_start + minutes_add) >= 60:
        minutes_start = (minutes_start + minutes_add) - 60
        if hours_start == 11 and not hours_add:
            if hour_mode == 'AM':
                hour_mode = 'PM'
                hours_start += 1
            else:
                hour_mode = 'AM'
                hours_start += 1
                day_count += 1
        elif hours_start == 12 and not hours_add:
            hours_start = 1
        elif hours_add >= 1:
            if hours_start == 11:
              if hour_mode == 'AM':
                hour_mode = 'PM'
                hours_start += 1
              else:
                hour_mode = 'AM'
                hours_start += 1
                day_count += 1
            elif hours_start == 12:
                hours_start = 1
            
    else:
        minutes_start = minutes_start + minutes_add
        
    if minutes_start < 10:
        minutes_start = '0' + str(minutes_start)
    # addition of hours
    if hours_add:
        while hours_add != 0:
            if hours_start == 11:
                if hour_mode == 'AM':
                    hour_mode = 'PM'
                    hours_start = 12
                    hours_add -= 1
                    if hours_add >= 1:
                        hours_add -= 1
                        hours_start = 1
                    else:
                        hours_start = 12
                else:
                    hour_mode = 'AM'
                    day_count += 1
                    hours_start = 12
                    hours_add -= 1
                    if hours_add  >= 1:
                        hours_add  -= 1
                        hours_start = 1
                    else:
                        hours_start = 12
            elif hours_start == 12:
                hours_start = 1
                hours_add -= 1
            else:
                hours_start += 1
                hours_add -= 1
                
    hours_start = str(hours_start)
    total_days = day_count
    #Day calculation
    if day:
        week = [
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
            'Sunday'
        ]
        starting_day = week.index(day.capitalize())

        if not day_count == 0:
            while not day_count == 0:
                if starting_day >= 6:
                    starting_day = 0
                    day_count -= 1
                else:
                    starting_day += 1
                    day_count -= 1

        end_day = week[starting_day]
    #Formating end string
    if day:
        if total_days == 1:
            final_format = '{}:{} {}, {} (next day)'.format(
                hours_start, minutes_start, hour_mode, end_day)
        elif total_days > 1:
            final_format = '{}:{} {}, {} ({} days later)'.format(
                hours_start, minutes_start, hour_mode, end_day, total_days)
        else:
            final_format = '{}:{} {}, {}'.format(hours_start, minutes_start,
                                                 hour_mode, end_day)
    else:
        if total_days == 1:
            final_format = '{}:{} {} (next day)'.format(
                hours_start, minutes_start, hour_mode)
        elif total_days > 1:
            final_format = '{}:{} {} ({} days later)'.format(
                hours_start, minutes_start, hour_mode, total_days)
        else:
            final_format = '{}:{} {}'.format(hours_start, minutes_start,
                                             hour_mode)
    return print(final_format)

add_time("11:59 PM", "24:05")