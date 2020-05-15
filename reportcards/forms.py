from django import forms
from .models import Student, Subject, Paper

class StudentRegistraionForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = '__all__'
