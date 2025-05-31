from django.shortcuts import render


def index(request):
    return render(request, 'Layout/pages/index.html')
