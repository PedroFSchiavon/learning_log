from django.shortcuts import render


# Create your views here.
def index(request):
    '''Página inicial de Learning Logs'''
    return render(request, 'learning_logs/index.html')
