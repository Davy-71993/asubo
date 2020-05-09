from django.shortcuts import render

def gaming(request):
    return render(request, 'gaming/index.html')

def game(request):
    return render(request, 'gaming/draft.html')

