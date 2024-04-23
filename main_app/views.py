from django.shortcuts import render, redirect
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm

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
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form
    })

def add_feeding(request, cat_id):
  # create a ModelForm instance using the data in request.POST
  submitted_form = FeedingForm(request.POST)
  # validate the form
  if submitted_form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = submitted_form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)


class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    success_url = '/cats/{id}'

class CatUpdate(UpdateView):
  model = Cat
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ('description', 'age')
  success_url = '/cats/{id}'

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats'

