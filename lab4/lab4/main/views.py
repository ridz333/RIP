from django.shortcuts import render, get_object_or_404
from .models import Main
#from .db import db

def main(request):
    return render(request, 'main/home.html', {'data': Main.objects.all()})

def item(request,id,slug):
    model = get_object_or_404(Main, id=id, slug=slug)
    return render(request, "main/detail.html", context={'model': model})
"""
def reg(request):
    database = db(dbname='artur',password='1')
    name = request.GET.get('name')
    login = request.GET.get('login')
    password = request.GET.get('password')

    database.insert(
        'Users',
        name = name,
        login = login,
        password = password
    )
    return render(request, 'main/home.html', {'data': Main.objects.all()})

def login(request):
    database = db(dbname='artur', password='1')
    login = request.GET.get('login')
    password = request.GET.get('password')

    database.query(
        'SELECT * FROM Users WHERE login=\'{}\''.format(login)
    )
"""