from django.shortcuts import render
from .models import Solution

def index(request):
    solutions = Solution.objects.all().order_by('name')
    context = {
        'solutions': solutions,
    }
    return render(request, 'mainapp/index.html', context)
