from datetime import datetime
from calendar import HTMLCalendar
from .models import Event



class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, day, events):
        events_per_day = len(events.filter(fro_date__day=day))
        d = '<div class="ents">\n'
        
        if events_per_day > 0:
            d += f'<button class="ebtn">{events_per_day}</button></div>'

        if day != 0:
            return f"<td class='day-cell'><a class='day' href='/calendar/day/?d={day}&m={self.month}&y={self.year}'>{day}</a> {d}</td>"
        return '<td></td>'

    def formatweek(self, theweek, events):
        week =''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr>{week}</tr>'

    def formatmonth(self, withyear = True):
        events = Event.objects.filter(fro_date__year = self.year, fro_date__month =self.month)
        cal = f'<table border="0"class="table table-bordered">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'

        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'

        return cal

