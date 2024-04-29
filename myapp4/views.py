from django.shortcuts import render,redirect
from .models import has
from .forms import myhas

def new(request):
    form=myhas()
    if request.method=='POST':
       form=myhas(request.POST)
       if form.is_valid():
           form.save()
           return redirect('/new')
    else:
        say=has.objects.all()
        form=myhas()
    return render(request,'index.html',{'form':form,'say':say})

       

