from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Contents
from django.shortcuts import redirect
from .forms import ContentsForm

# Create your views here.

def index(request):
    texts = Contents.objects.all()
    foods = ['apple', 'banana', 'coconut']
    pick = random.choice(foods)
    info = {
        'name': 'kildong',
        'age': 20,
    }
    context = {
        'pick': pick,
        'foods': foods,
        'info': info,
        'texts': texts,
    }
    
    return render(request, 'report_main/index.html', context)


def detail(request, pk):
    text = Contents.objects.get(id=pk)
    context = {
        'text': text
    }

    return render(request, 'report_main/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ContentsForm(request.POST)
        if form.is_valid():
            text = form.save()

            return redirect('report_main:detail', text.pk)
        
    else:
        form = ContentsForm()

    context = { 'form': form }
    return render(request, 'report_main/create.html', context)


def delete(request, pk):
    text = Contents.objects.get(id=pk)
    if request.method == 'POST':
        text.delete()

        return redirect('report_main:index')
    
    else:
        return redirect('report_main:detail', text.pk)


def update(request, pk):
    text = Contents.objects.get(id=pk)
    if request.method == 'POST':
        form = ContentsForm(request.POST, instance=text)
        if form.is_valid():
            form.save()
            return redirect('report_main:detail', text.pk)

        return redirect('report_main:detail', text.pk)
    
    else:
        form = ContentsForm(instance=text)

    context = {'form': form}
    return render(request, 'report_main/update.html', context)

