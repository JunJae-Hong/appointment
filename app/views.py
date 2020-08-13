rom django.shortcuts import render, redirect, get_object_or_404
from .models import Board
import datetime

# Create your views here.
def index(request):
    x=Board.objects
    return render(request, 'index.html',{'x':x})
    
def create(request):
    return render(request, 'create.html')

def new(request):
    x = Board() #x는 변수 
    #x.title = request.GET['title']
    #x.text = request.GET['text']
    #x.category = request.GET['category']
    x.save()
    return redirect('/')

def read(request, Board_id):
    read = get_object_or_404(Lol, pk=Board_id)
    return render(request, 'read.html', {'read':read})

def delete(request, Board_id):
    x = get_object_or_404(Lol, pk=Board_id)
    x.delete()
    return redirect('/')
    
def update(request, Board_id):
    x = get_object_or_404(Lol, pk=Board_id)
    return render(request,'update.html',{'x':x})

def updat(request, Board_id):
    x = get_object_or_404(Lol, pk=Board_id)
    #x.title = request.GET['title']
    #x.text = request.GET['text']
    #x.category = request.GET['category']
    #x.date = datetime.datetime.now()
    x.save()
    return redirect('/'+str(Board_id))