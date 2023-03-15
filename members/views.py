from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
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


# def search(request):
#     query_dict=request.GET
#     query=query_dict("q")
#     search_obj=None
#     if id is not None:
#         search_obj=Member.objects.get(pk=query)
#     context={"data":search_obj}
#     return render(request,'members/search.html',context)
# Create your views here.
# from django.views.generic import ListView
# class SearchView(ListView):
#     model=Member
#     template='members/search.html'
#     context_object_name='search'
#     def get_queryset(self):
#         query=self.request.GET.get('q')
#         return Member.objects.filter(firstname__icontains=query)
def search(request):
    if 'q' in request.GET:
        q=request.GET['q']
        data=Member.objects.filter(firstname__icontains=q)
    else:
        data=Member.objects.all()
    context={
        'data':data
    }    
    return render(request,'members/search.html', context)
from .forms import MemberForm
def register(request):
   form=MemberForm()
   if request.method == 'POST':
       form=MemberForm(request.POST)
       if form.is_valid():
        # firstname = form.cleaned_data['firstname'],  
        # lastname = form.cleaned_data['lastname'],  
        # gender = form.cleaned_data['gender'],  
        # joined_date=  form.cleaned_data['joined_date']  
        form.save()
        return  redirect('/')
   context={'form':form}   
   return render(request, 'members/new_member.html', context)