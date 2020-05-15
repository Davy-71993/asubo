
from reportcards.models import MarkList, Result, Score, Student
from datetime import datetime, timedelta, date

def has_students(klass, stream = None):
    if stream:
        stds = get_students(klass=klass, stream=stream)
        if stds.count():
            return True

        else:
            return False

    else:
        stds = get_students(klass=klass)
        if stds.count():
            return True

        else:
            return False

def get_students(klass, stream=None):
    if stream:
        stds = Student.objects.filter(klass=klass, stream=stream)
        return stds

    else:
        stds = Student.objects.filter(klass=klass)
        return stds

def create_marklist(term, klass, stream):
    year = datetime.now().year
    marklist = MarkList(year=year, term=term, klass=klass, stream=stream)
    message = ''
    mkl = None

    if has_students(klass=klass, stream=stream):
        marklist.save()
        mkl = MarkList.objects.get(year=year, term=term, klass=klass, stream=stream)
        students = mkl.students
        for student in students:
            res = Result(marklist=mkl, student=student)
            if res in Result.objects.all():
                pass
            else:
                res.save()
                for sub in student.subjects:
                    s = Score(subject=sub, student=student, marklist=mkl)
                    if s in Score.objects.all():
                        pass
                    else:
                        s.save()
    else:
        pass
    return mkl

def allocate_house():
    aus = len(Student.objects.filter(house = 'Australia'))
    bra = len(Student.objects.filter(house = 'Brazil'))
    can = len(Student.objects.filter(house = 'Canada'))
    fra = len(Student.objects.filter(house = 'France'))
    jap = len(Student.objects.filter(house = 'Japan'))
    nig = len(Student.objects.filter(house = 'Nigeria'))

    list = [aus, bra, can, fra, jap, nig]
    list.sort()

    if list[0] == aus:
        return 'Australia'
    elif list[0] == bra:
        return 'Brazil'
    elif list[0] == can:
        return 'Canada'
    elif list[0] == fra:
        return 'France'
    elif list[0] == jap:
        return 'Japan'
    elif list[0] == nig:
        return 'Nigeria'
    else:
        return ''

def days_arr(date1,date2):
    for n in range(int((date2 - date1).days)+1):
        yield date1+timedelta(n)

def get_dates(d1, d2):
    ls = []
    for dt in days_arr(d1, d2):
        ls.append(dt.strftime("%Y-%m-%d"))

    return ls
 
def week():
    yr = datetime.now().year
    mon = datetime.now().month
    day = datetime.now().day
    date_str = f'{yr}-{mon}-{day}'
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    
    start_of_week = date_obj - timedelta(days=date_obj.weekday())  # Monday
    end_of_week = start_of_week + timedelta(days=6)  # Sunday

    first_last = [
        start_of_week,
        end_of_week
    ]

    return first_last

def str_week_day(d):
    str_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturtday', 'Sunday']
    int_day = d.weekday()
    return str_days[int_day]












