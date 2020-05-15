import datetime
from django.shortcuts import render, redirect
from .models import MarkList, MarkListSetUp, Score, Result, Student, Subject, Paper
from mainapp import helper
from . import forms

## marklist
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
                    mkl = helper.create_marklist(term=term, klass=klass, stream=stream)

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

## students
def add(request):
    subjects = Subject.objects.all()
    form = forms.StudentRegistraionForm()

    if request.method == 'POST':
        if request.FILES.get('std_file'):
            return redirect('students')

        form = forms.StudentRegistraionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            '''
                Each time we create a student we need to check if this student's class stream has any marklist
                If so, then a result should be appended to the marklist for this student. 
            '''
            return redirect('register_student')

    context = {
        'form': form,
        'subjects': subjects,
    }
    return render(request, 'reportcards/add.html', context)

def import_students(request):

    if request.method == 'POST':
        std_file = request.FILES['std_file']

        df = pandas.read_excel(std_file)
        df.fillna('')
        rows = len(df)
        print(df)

        i = 0
        while i < rows:
            df['Other Names'].fillna('', inplace=True)
            df['Sex'].fillna('', inplace=True)
            print(df['Other Names'][i])
            Student.objects.create(
                sir_name = df['Sir Name'][i],
                given_name = df['Given Name'][i],
                other_names = df['Other Names'][i],
                sex = df['Sex'][i],
                klass = df['Class'][i],
                stream = df['Stream'][i],
                house = helper.allocate_house()
            )

            i += 1

    context = {}
    return render(request, 'reportcards/import.html', context)

def students(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'reportcards/students.html', context)

def student(request, pk):
    student = Student.objects.get(id=pk)
    form = forms.StudentRegistraionForm(instance=student)

    if request.method == 'POST':
        form = forms.StudentRegistraionForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')

    context = {
        'form': form,
        'student': student,
    }
    return render(request, 'reportcards/student.html', context)

def delete_student(request, pk):
    student = Student.objects.get(id = pk)

    if request.method == 'POST':
        student.delete()
        return redirect('students')

    context ={
        'instance': student,
        'object': 'Student'
    }
    return render(request, 'mainapp/delete.html', context)

def view_by_class(request, cl):
    students = Student.objects.filter(klass = cl)

    context = {
        'students': students,
        'class': cl,
    }
    return render(request, 'reportcards/view_by_class.html', context)

def view_by_stream(request, cl, strm):
    students = Student.objects.filter(klass = cl, stream = strm)

    context = {
        'students': students,
        'class': cl,
        'stream': strm,
    }
    return render(request, 'reportcards/view_by_stream.html', context)

def view_by_house(request, hs):
    students = Student.objects.filter(house = hs)

    context = {
        'students': students,
        'hs': hs,
    }
    return render(request, 'reportcards/view_by_house.html', context)

## subjects and papers
def subjects(request):
    subs = Subject.objects.all()
    sub_form = SubjectForm()

    if request.method == 'POST':
        sub_form = SubjectForm(request.POST)
        if sub_form.is_valid():
            sub_form.save()
            pass

    context ={
        'subjects': subs,
        'subject_form': sub_form,
    }

    return render(request, 'mainapp/subjects.html', context)

def add_paper(request, pk, px):
    subject = Subject.objects.get(id = pk)
    paper_form = PaperForm()
    paper_form.fields['subject'].value = subject
    if request.method == 'POST':
        paper_form = PaperForm(request.POST)
        if paper_form.is_valid():
            paper_form.save()
            return redirect('subjects')

    context ={
        'subject': subject,
        'level': px,
        'paper_form': paper_form,
    }
    return render(request, 'mainapp/add_paper.html', context)

def update_subject(request, pk):
    subject = Subject.objects.get(id = pk)
    form = SubjectForm(instance=subject)

    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subjects')

    context = {
        'form':form,
        'instance': subject,
    }
    return render(request, 'mainapp/update.html', context)

def delete_subject(request, pk):
    subject = Subject.objects.get(id = pk)

    if request.method == 'POST':
        subject.delete()
        return redirect('subjects')

    context ={
        'instance': subject,
        'object': 'Subject'
    }
    return render(request, 'mainapp/delete.html', context)

def edit_paper(request, pk):
    paper = Paper.objects.get(id = pk)
    form = PaperForm(instance=paper)

    if request.method == 'POST':
        form = PaperForm(request.POST, instance=paper)
        if form.is_valid():
            form.save()
            return redirect('subjects')

    context = {
        'form':form,
        'instance': paper,
    }
    return render(request, 'mainapp/update.html', context)

def delete_paper(request, pk):
    paper = Paper.objects.get(id = pk)

    if request.method == 'POST':
        paper.delete()
        return redirect('subjects')

    context ={
        'instance': paper,
        'object': 'Paper'
    }
    return render(request, 'mainapp/delete.html', context)


