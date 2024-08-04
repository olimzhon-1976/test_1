from django.shortcuts import render

def home(request):
    return render(request, 'cityinfo/home.html')

def news(request):
    return render(request, 'cityinfo/news.html')

def management(request):
    return render(request, 'cityinfo/management.html')

def facts(request):
    return render(request, 'cityinfo/facts.html')

def contacts(request):
    return render(request, 'cityinfo/contacts.html')

def history(request):
    return render(request, 'cityinfo/history.html')

def history_people(request):
    return render(request, 'cityinfo/history_people.html')

def history_photos(request):
    return render(request, 'cityinfo/history_photos.html')