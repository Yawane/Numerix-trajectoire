from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    if request.method == 'POST':
        items = []
        for i in range(1, 10):
            a = request.POST.get(f"item{i}")
            items.append(a)
            print(f"item{i} :", a)

    return render(request, 'index.html', context={'items': items})

