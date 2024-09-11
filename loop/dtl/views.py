# views.py
from django.shortcuts import render


def home(request):
    return render(request, 'dtls/home.html')

def catalog(request):
    context = {
        'To Kill a Mockingbird': 'Harper Lee',
        '1984': 'George Orwell',
        'Moby Dick': 'Herman Melville',
        'The Great Gatsby': 'F. Scott Fitzgerald',
    }
    return render(request, 'dtls/catalog.html', context)
