from django.db import models

class Student(models.Model):
    class_choices = (
        ('S.1', 'S.1'),
        ('S.2', 'S.2'),
        ('S.3', 'S.3'),
        ('S.4', 'S.4'),
        ('S.5', 'S.5'),
        ('S.6', 'S.6'),
    )

    streams = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('S', 'S'),
    )

    sex_choices = (
        ('Female', 'Female'),
        ('Male', 'Male')
    )

    house_choices = (
        ('Australia', 'Australia'),
        ('Brazil', 'Brazil'),
        ('Canada', 'Canada'),
        ('France', 'France'),
        ('Japan', 'Japan'),
        ('Nigeria', 'Nigeria')
    )

    sir_name = models.CharField(max_length=50)
    given_name = models.CharField(max_length=50)
    other_names = models.CharField(max_length=50, null=True, blank=True)
    sex = models.CharField(max_length=8, choices=sex_choices)
    passport_photo = models.ImageField(upload_to='passports', blank=True, null=True)
    klass = models.CharField(max_length=5, choices=class_choices)
    stream = models.CharField(max_length=10, choices=streams)
    house = models.CharField(max_length=10, choices=house_choices, blank=True, null=True)
    # subjects = models.ManyToManField(Subject, default= Subject.objects.filter(is_compulsary=True))
    date_added = models.DateTimeField(auto_now=True)
    scores = {}

    def __str__(self):
        return self.sir_name

    @property
    def full_names(self):
        if self.other_names != None:
            return f'{self.sir_name} {self.given_name} {self.other_names}'

        else:
            return f'{self.sir_name} {self.given_name}'

    @property
    def subjects(self):
        alevel_classes = ['S.5', 'S.6']
        if self.klass in alevel_classes:
            return Subject.objects.filter(alevel = True)
        else:
            return Subject.objects.filter(olevel = True)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=6)
    alevel = models.BooleanField(default= False)
    olevel = models.BooleanField(default= False)
    olevel_code = models.CharField(max_length=10, blank=True, null=True)
    alevel_code = models.CharField(max_length=10, blank=True, null=True)
    is_compulsary = models.BooleanField(default=False)

    @property
    def olevel_papers(self):
        return Paper.objects.filter(subject = self, level = 'Olevel')

    @property
    def alevel_papers(self):
        return Paper.objects.filter(subject = self, level = 'Alevel')

    def __str__(self):
        return self.name

class Paper(models.Model):
    level_choices = (
        ('Alevel', 'Alevel'),
        ('Olevel', 'Olevel')
    )
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    level = models.CharField(max_length= 10, choices= level_choices)

    def __str__(self):
        return f'{self.subject} {self.name}'

class MarkList(models.Model):
    year = models.IntegerField()
    term = models.CharField(max_length=10)
    klass = models.CharField(max_length=10)
    stream = models.CharField(max_length=10)

    def smt(self, x=0):
        return (self.year) + x

    @property
    def level(self):
        a = ['S.5', 'S.6']
        if self.klass in a:
            return 'A'
        else:
            return 'O'

    @property
    def students(self):
        if self.stream:
            return Student.objects.filter(klass=self.klass, stream=self.stream)
        else:
            return Student.objects.filter(klass=self.klass)

    def __str__(self):
        return f'{self.klass} {self.stream} {self.term} {self.year}'

class MarkListSetUp(models.Model):
    marklist = models.OneToOneField(MarkList, on_delete=models.CASCADE)
    include_papers = models.BooleanField(default=False)
    num_exams = models.IntegerField()

    def __str__(self):
        return f'{ self.marklist } SETUP'

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marklist = models.ForeignKey(MarkList, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    value1 = models.FloatField(blank=True, null=True)
    value2 = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{ self.student } { self.subject } Score'

class Result(models.Model):
    marklist = models.ForeignKey(MarkList, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{ self.student }'s Marks"
    
    @property
    def scores(self):
        std_scores = Score.objects.filter(marklist = self.marklist, student = self.student)
        scores = []

        for score in std_scores:
            xml ={ 
                'subject': score.subject,
                'value': score.value,
                'value1': score.value1,
            }
            scores.append(xml)
        return scores

    @property
    def all_scores(self):
        std_scores = Score.objects.filter(marklist = self.marklist, student = self.student)
        scores = {
            'student': self.student,
        }

        for score in std_scores:
            xml ={ 
                score.subject.abbr: {
                    'subject': score.subject,
                    'value': score.value,
                    'value1': score.value1,
                },
            }
            scores.update(xml)
        return scores

    def scores_by_subject(self, subject):
        scores = Score.objects.get(marklist = self.marklist, subject = subject, student = self.student)
        return scores
   
    


