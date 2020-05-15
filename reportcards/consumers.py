# reportcards/consumers.py
import json
import datetime
from channels.generic.websocket import WebsocketConsumer
from .models import Score, MarkList
from students.models import Student, Subject

class ScoreConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        val = text_data_json['value']
        mkl = text_data_json['mkl']
        std = text_data_json['std']
        name = text_data_json['name']
        sub = text_data_json['sub']

        score = Score.objects.get(
            student = Student.objects.get(id = std),
            marklist = MarkList.objects.get(id = mkl),
            subject = Subject.objects.get(id=sub)
        )

        if score:
            if name == 'value':
                score.value = val
                score.save()
                self.send(text_data=json.dumps({
                    'message': score.value
                }))
            elif name == 'value1':
                score.value1 = val
                score.save()
                self.send(text_data=json.dumps({
                    'message': score.value1
                }))
            else:
                self.send(text_data=json.dumps({
                    'message': 'The name was not passed'
                }))
        else:
            self.send(text_data=json.dumps({
                'message': 'not found'
            }))
    
class SubjectScoreConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        val = text_data_json['value']
        mkl = text_data_json['mkl']
        std = text_data_json['std']
        name = text_data_json['name']
        sub = text_data_json['sub']

        score = Score.objects.get(
            student = Student.objects.get(id = std),
            marklist = MarkList.objects.get(id = mkl),
            subject = Subject.objects.get(id=sub)
        )

        if score:
            if name == 'value':
                score.value = val
                score.save()
                self.send(text_data=json.dumps({
                    'message': score.value
                }))
            elif name == 'value1':
                score.value1 = val
                score.save()
                self.send(text_data=json.dumps({
                    'message': score.value1
                }))
            else:
                self.send(text_data=json.dumps({
                    'message': 'The name was not passed'
                }))
        else:
            self.send(text_data=json.dumps({
                'message': 'not found'
            }))
    
class StreamScoreConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        val = text_data_json['value']
        mkl = text_data_json['mkl']
        std = text_data_json['std']
        name = text_data_json['name']
        sub = text_data_json['sub']

        score = Score.objects.get(
            student = Student.objects.get(id = std),
            marklist = MarkList.objects.get(id = mkl),
            subject = Subject.objects.get(id=sub)
        )

        if score:
            if name == 'value':
                score.value = val
                score.save()
                self.send(text_data=json.dumps({
                    'message': score.value
                }))
            elif name == 'value1':
                score.value1 = val
                score.save()
                self.send(text_data=json.dumps({
                    'message': score.value1
                }))
            else:
                self.send(text_data=json.dumps({
                    'message': 'The name was not passed'
                }))
        else:
            self.send(text_data=json.dumps({
                'message': 'not found'
            }))      

class ClassScoreConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        
        val = text_data_json['value']
        int_class = text_data_json['int_class']
        std = text_data_json['std']
        name = text_data_json['name']
        sub = text_data_json['sub']
        term = text_data_json['term']

        klass = f'S.{int_class}'
        year = datetime.datetime.now().year

        student = Student.objects.get(id = std)
        mkl = MarkList.objects.get(klass=klass, term=term, year=year, stream=student.stream)

        score = Score.objects.get(
            student = student,
            marklist = mkl,
            subject = Subject.objects.get(id=sub)
        )
        
        if score:
            if name == 'value':
                score.value = val
                score.save()
                self.send(text_data=json.dumps({
                    'message': score.value
                }))
            elif name == 'value1':
                score.value1 = val
                score.save()
                self.send(text_data=json.dumps({
                    'message': score.value1
                }))
            else:
                self.send(text_data=json.dumps({
                    'message': 'The name was not passed'
                }))
        else:
            self.send(text_data=json.dumps({
                'message': 'not found'
            }))






























