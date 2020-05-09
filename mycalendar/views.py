from datetime import date

from django.shortcuts import render
from django.utils.html import mark_safe

from .utils import Calendar, Day
from .models import Event

def year(request):
    today = date.today()
    yr = today.year
    months = [1,2,3,4,5,6,7,8,9,10,11,12]

    cal = []

    for i in months:
        m = Calendar(yr, i).formatmonth(withyear = True)
        cal.append(
            mark_safe(m)
        )
    context = {
        'calendar': cal,
    }
    return render(request, 'myCalendar/year.html', context)

def month(request):
    today = date.today()
    yr = today.year
    m = today.month
    if request.GET.get('month'):
        m = int(request.GET.get('month'))
        if m <= 0:
            m = 12
        if m > 12:
            m = 1

    cal = Calendar(yr, m).formatmonth(withyear = True)

    context = {
        'calendar': mark_safe(cal),
        'm_next': m+1,
        'm_prev': m-1,
    }
    return render(request, 'myCalendar/month.html', context)

def week(request):
    pass

def day(request):
    today = date.today()
    day = today
    d = request.GET.get('d') 
    m = request.GET.get('m')
    y = request.GET.get('y')
    if d and m and y:
        day = date(int(y), int(m), int(d))

    events = Event.objects.filter(fro_date = day)
    html = Day(day=day, events=events).display()
    context = {
        'today': day,
        'html': mark_safe(html),
    }
    return render(request, 'myCalendar/day.html', context)


def period(request):
    pass

# Create your views here.
