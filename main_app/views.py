from django.shortcuts import render
from .models import Cat

# Create your views here.
#temporary database - remove this after adding cat model
cats = [
    {'name': 'lolo', 'breed': 'tabby', 'description': 'furry littel demon', 'age': 3},
    {'name': 'sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2}
]

def home(request): 
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

def cats_index(request): 
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {
        'cats': cats
    })


def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {
        'cat': cat
    })