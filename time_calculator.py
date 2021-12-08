from datetime import datetime, timedelta


weekdays = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
    'sunday': 6
}


class Interval():
    def __init__(self, inteval):
        items = inteval.split(':')
        hours = items[0]
        minutes = items[1]

        if(not hours.isdigit()):
            raise Exception('Invalid hour')

        if(not minutes.isdigit()):
            raise Exception('Invalid minute')

        self.days = int(int(hours)/24)
        self.hours = int(hours)%24
        self.minutes = int(minutes)
        self.interval = timedelta(days=self.days, hours=self.hours, minutes=self.minutes)


def add_time(start, interval, weekday=''):
    weekday = weekday.lower()
    start = datetime.strptime(start, '%I:%M %p')
    if(len(weekday)):
        start += timedelta(days=weekdays[weekday])

    interval = Interval(interval).interval
    final = start + interval

    days_format = ''
    days = final.day - start.day
    if(days):
        if(days > 1):
            days_format = f' ({days} days later)'
        else:
            days_format = f' (next day)'

    if(len(weekday)):
        final_time = final.strftime('%I:%M %p, %A')
    else:
        final_time = final.strftime('%I:%M %p')

    result = f'{final_time}{days_format}'
    if(result[0] == '0'):
        result = result[1:]

    return result
