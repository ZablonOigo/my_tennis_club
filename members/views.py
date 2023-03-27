from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from . models import Member
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def index(request):
    mydata=Member.objects.all()
    context={'mydata':mydata}
    return render(request, 'members/index.html', context)
@login_required
def detail(request,id):
    queryset=Member.objects.filter(firstname=request.user)
    data=get_object_or_404(Member,pk=id)
    context={'data':data}
    return render(request, 'members/detail.html', context)
# def search(request):
#     if 'q' in request.GET:
#         q=request.GET['q']
#         data=Member.objects.filter(firstname__icontains=q)
#     else:
#         data=Member.objects.all()
#     context={
#         'data':data
#     }    
#     return render(request,'members/search.html', context)
from django.views.generic import ListView
# class SearchView(ListView):
#     model=Member
#     template_name='members/search.html'
#     def query_set(self):
#         query=self.request.GET.get('q')
#         object_list=Member.objects.filter(Q(firstname__icontains=query)|
#                                      Q(lastname__icontains=query))
        
#         return object_list
@login_required
def search(request):
    if request.method=='POST':
        searched=request.POST['q']
        data=Member.objects.filter(Q(firstname__contains=searched)|Q(
            lastname__contains=searched
        ))
        context={'searched':searched ,'data':data }
        return render(request,'members/search.html', context)
    
    else:
           return render(request,'members/search.html')


from .forms import MemberForm
def register(request):
   if request.method =='GET':
       form=MemberForm()
       context={'form':form}
       return render(request, 'members/new_member.html', context)
   elif request.method == 'POST':
       form=MemberForm(request.POST)
       if form.is_valid():
        context={'form':form}   
        form.save()
        return  redirect('members:index')
       else:
           return render(request, 'members/new_member.html', context)
       
from django.contrib import messages
@login_required
def delete_member(request,id):
     queryset=Member.objects.filter(firstname=request.user)
     mydata=get_object_or_404(Member,id=id)
     context={'mydata':mydata}
     if request.method =='GET':
         return render(request,'members/delete_confirm.html',context)
     
     elif request.method =='POST':
         mydata.delete()
         messages.success(request,'Member was removed')
         return redirect('members:index')
     
@login_required
def update_member(request,id):
    queryset=Member.objects.filter(firstname=request.user)
    post=get_object_or_404(Member,id=id)
    context={'form':MemberForm(instance=post),'id':id}
    if request.method =='GET':
        return render(request,'members/new_member.html',context)
    elif request.method =='POST':
        form=MemberForm(request.POST,instance=post)
        if form.is_valid():
         context={'form':form}
         form.save()
         messages.success(request,'Updated sucessfully')
         return redirect('members:index')
        else:
            return render(request,'members/new_member.html',context) 
         
     
    
    
    

     
   