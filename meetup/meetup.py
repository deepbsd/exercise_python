from datetime import date
from calendar import monthrange

class MeetupDayException(Exception):
    def __init__(self, message):
        self.message = message

def meetup_day(yr, mo, day, when):
    count = []
    w2d = {"Monday":1, "Tuesday":2, "Wednesday":3, "Thursday":4, "Friday":5, "Saturday":6, "Sunday":7}
    seq = {"1st": range(1,8), "teenth": range(13,20), "2nd": range(8,15), "last": range(25,32), "3rd": range(15,22), "4th": range(22,32), "5th": range(25,32)}

    if mo == 2 and when in ['last', '4th', '5th']:
        period = range(monthrange(yr,mo)[1]-6, monthrange(yr, mo)[1]+1)
    else:
        period = seq[when]
    if mo == 2 and when == "5th":
        for n in range(monthrange(yr,mo)[0],monthrange(yr,mo)[1]):
            count.append(n)
            if len(count) < 5:
                raise MeetupDayException('Not a Valid Date.')
    for n in period:
        if date(yr, mo, n).isoweekday() == w2d[day]: return date(yr, mo, n)

    raise MeetupDayException('Not a Valid Date.')
