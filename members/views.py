from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Member
from django.db.models import Q

def index(request):
    mydata=Member.objects.all()
    context={'mydata':mydata}
    return render(request, 'members/index.html', context)

def detail(request,id):
    data=get_object_or_404(Member,pk=id)
    context={'data':data}
    return render(request, 'members/detail.html', context)

def search(request):
    if request.method == 'POST':
        searched=request.POST['searched']
        mydata=Member.objects.filter(entry__firstname__name__isnull=True)
        return render(request, 'members/search.html',{'searched':searched,'mydata':mydata})

    else:
        return render(request, 'members/search.html')
    
# Create your views here.
