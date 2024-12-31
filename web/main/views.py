from django.shortcuts import render


def inbox(request):
    return render(request, 'main/inbox.html')

def today(request):
    return render(request, 'main/today.html')