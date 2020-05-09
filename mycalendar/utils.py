from datetime import datetime, date
from calendar import HTMLCalendar
from .models import Event



class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, day, events):
        today = date.today()
        dc = ''
        if day != 0:
            td =date(self.year, self.month, day)
            if today == td:
                dc = 'today'

        events_per_day = len(events.filter(fro_date__day=day))
        d = '<div class="ents">\n'
        
        if events_per_day > 0:
            d += f'<button class="ebtn">{events_per_day}</button></div>'

        if day != 0:
            return f"<td class='day-cell {dc}'><a class='day' href='/calendar/day/?d={day}&m={self.month}&y={self.year}'>{day}</a> {d}</td>"
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

class Day():
    def __init__(self, day=None, events=None):
        self.day = day
        self.events = events
        super(Day, self).__init__()

    def display(self):
        if self.events != None and self.events.count():
            html = '<table class="table table-responsive table-striped"><thead><th></th>'
            hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
            
            for hr in hours:
                html += f'<th>{hr}:00</th>'

            html += f'</thead><tbody>'

            for event in self.events:
                html += f'<tr><td>{event}</td>'
                for hr in hours:
                    now = datetime(self.day.year, self.day.month, self.day.day, hr ).hour
                    fro = event.fro_time.hour
                    to = event.to_time.hour

                    if now >= fro and now <= to:
                        html += f'<td class="bg-info"></td>'
                    else:
                        html += f'<td></td>'
     
            return html + f'</tr></tbody></table>'
        else:
            return f"<h2 class='text-center text-warning'>You don't have any events scheduled.</h2><div class='container'><a class='btn btn-outline-primary' href='#'>Create New Events</a></div>"
