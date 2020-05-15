import datetime
from django.shortcuts import render, redirect
from .models import MarkList, MarkListSetUp, Score, Result, Student, Subject, Paper
from mainapp import helper

def creat_marklist(request):
    year = datetime.datetime.now().year
    marklists = MarkList.objects.filter(year=year)
    massage = ''
    if request.method == 'POST':
        klass = request.POST.get('class')
        stream = request.POST.get('stream')
        term = request.POST.get('term')

        if stream:
            test_marklist = MarkList.objects.filter(year=year, term=term, klass=klass, stream=stream)
            if test_marklist.count():
                massage = 'Marklist already exists, please chect in the list on your left'
            else:
                if helper.has_students(klass=klass, stream=stream):
                    mkl = helper.create_marklist(term=term, klass=klass, stream=stream).marklist

                    return redirect('setup_marklist', mkl = mkl.id) 
                else:
                    massage = f'There are no students registered in { klass } { stream } please add students to continue'
        else:
            if helper.has_students(klass=klass):
                return redirect('class_marklist', klass = klass.split('.')[1], term = term.split(' ')[1])
            else:
                massage = f'There are no students registered in { klass } { stream } please add students to continue'

    context ={
        'year': year,
        'marklists': marklists,
        'massage': massage,
    }
    return render(request, 'reportcards/creat_marklist.html', context)

def setup_marklist(request, mkl):
    marklist = MarkList.objects.get(id=mkl)

    if request.method == 'POST':
        num_exams = request.POST.get('exams')
        include_pappers = request.POST.get('papers')

        if include_pappers:
            setup = MarkListSetUp(
                marklist=marklist, 
                include_papers=True, 
                num_exams=num_exams
            )
            setup.save()
        else: 
            setup = MarkListSetUp(marklist=marklist, include_papers=False, num_exams=num_exams)
            setup.save()

        return redirect('creat_marklist')

    context = {
        'marklist': marklist,
    }
    return render(request, 'reportcards/setup.html', context)

def marklist(request, pk):
    year = datetime.datetime.now().year
    marklists = MarkList.objects.filter(year=year)
    mkl = MarkList.objects.get(id = pk)
    subs = Subject.objects.all()
    students = mkl.students

    if request.method == 'POST':
        student = request.POST.get('student')
        subject = request.POST.get('subject')

        if student:
            return redirect('marks_by_student', std=student, mkl=mkl.id)
            
        elif subject:
            return redirect('marks_by_subject', sub=subject, mkl=mkl.id)
            
        else:
            return redirect('home')


    context = {
        'marklist': mkl,
        'marklists': marklists,
        'students': students,
        'subjects': subs,
    }
    return render(request, 'reportcards/marklist.html', context)

def marks_by_subject(request, mkl, sub):
    marklist = MarkList.objects.get(id=mkl)
    subject = Subject.objects.get(id=sub)

    results = Result.objects.filter(marklist=marklist)
    scores = []
    for result in results:
        dict = {
            'score': result.scores_by_subject(subject),
        }
        scores.append(dict)

    context = {
        'marklist': marklist,
        'subject': subject,
        'results': results,
        'scores': scores,
    }
    return render(request, 'reportcards/marks_by_subject.html', context)

def marks_by_student(request, mkl, std):
    marklist = MarkList.objects.get(id=mkl)
    subjects = Subject.objects.all()
    student = Student.objects.get(id = std)

    result = Result.objects.filter(marklist=marklist, student=student).first()

    context = {
        'marklist': marklist,
        'subjects': subjects,
        'student': student,
        'scores': result.scores,
    }
    return render(request, 'reportcards/marks_by_student.html', context)

def marks_by_stream(request, mkl):
    marklist = MarkList.objects.get(id = mkl)
    results = Result.objects.filter(marklist = marklist)
    classes = ['S.6', 'S.5']

    if marklist.klass in classes:
        subjects = Subject.objects.filter(alevel=True)
    else:
        subjects = Subject.objects.filter(olevel=True)

    scores = []
    for result in results:
        dic = {
            'score': result.all_scores,
        }
        scores.append(dic)

    context = {
        'marklist': marklist,
        'results': results,
        'subjects': subjects,
        'scores': scores,
    }
    return render(request, 'reportcards/marks_by_stream.html', context)

def class_marklist(request, klass, term):
    year = datetime.datetime.now().year
    str_class = f'S.{ klass }'
    marklists = MarkList.objects.filter(klass = str_class, term = f'TERM {term}', year=year)
    scores = []
    a = ['S.5', 'S.6']

    if str_class in a:
            s = ['A', 'S']
            if len(marklists) == 2:
                pass
            elif len(marklists) < 2:
                for l in s:
                    mkl = MarkList(klass=str_class, stream=l, year=year)
                    if mkl in MarkList.objects.all():
                        pass
                    else:
                        if helper.has_students(klass=str_class, stream=l):
                            helper.create_marklist(term=f'TERM {term}', klass=str_class, stream=l)
                        else:
                            pass
            else:
                pass
    else:
        s = ['A', 'B', 'C']
        if len(marklists) == 3:
            pass
        elif len(marklists) < 3:
            for l in s:
                mkl = MarkList.objects.filter(klass=str_class, stream=l, year=year)
                if mkl.count():
                    pass
                else:
                    if helper.has_students(klass=str_class, stream=l):
                        helper.create_marklist(term=f'TERM {term}', klass=str_class, stream=l)
                    else:
                        pass
        else:
            pass
        
    marklists = MarkList.objects.filter(klass = str_class, term = f'TERM {term}', year=year)
    for marklist in marklists:
        for student in marklist.students:
            res = Result.objects.get(student=student, marklist=marklist)
            scores.append(res.all_scores)

    context = {
        'int_class': klass,
        'str_class': str_class,
        'scores':scores,
        'year': year,
        'term': f'TERM {term}'
    }
    return render(request, 'reportcards/class_marklist.html', context)



