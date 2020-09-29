from django.shortcuts import render

def index(request):
    # templates/frontend/index.html
    return render(request, 'frontend/index.html')
