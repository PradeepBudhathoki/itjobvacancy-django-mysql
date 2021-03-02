from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import VacancyForm
from .models import Vacancy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse

import mysql.connector as mc
con = mc.connect(host="localhost", user="root", passwd="", database='vacancy')
print('Successfully connected to database')
cur=con.cursor()

def vacancy_list(request):
    
    #data=Vacancy.objects.raw("SELECT * from itjob_vacancy WHERE vacancy_id=1001")
    #data=Vacancy.objects.raw("SELECT `vacancy_id`,`title`,`name` from itjob_vacancy A, itjob_category B WHERE  A.category_id = B.category_id ")
    data=Vacancy.objects.raw("SELECT * from itjob_vacancy ORDER BY `published_date` DESC ")
    #print(data)
    return render(request,"itjob/vacancy_list.html",{'vacancys':data})



#class VacancyListView(ListView):
    #paginate_by =3
    #model=Vacancy#what model to query;posts
    #template_name='itjob/vacancy_list.html'#<app>/post_list.html
    #context_object_name='vacancys'
    #ordering=['-published_date'] #-sign indicates newest to oldest


class VacancyDetailView(DetailView):
    model=Vacancy

def vacancy_delete(request,pk):
     
    #id = request.GET['id']
    #id = User.objects.get(id=id)
    print(pk)
    cur.execute("DELETE FROM `itjob_vacancy` where `vacancy_id` = {}".format(pk))
    con.commit()
    return redirect('vacancylist')




def vacancy_search(request):
    inputVar=request.POST.get('inputVar',)
    
    print(inputVar)
    data=Vacancy.objects.raw(" SELECT * FROM `itjob_vacancy` WHERE `title` =%s ",[inputVar] )
    
    return render(request,"itjob/vacancy_search.html",{'vacancys':data})


class VacancyCreateView(LoginRequiredMixin, CreateView):
    model=Vacancy
    fields='__all__'
    #success_url=reverse_lazy('blog-home')

    def form_valid(self,form):
        
        return super().form_valid(form)


class VacancyUpdateView(LoginRequiredMixin, UpdateView):
    model=Vacancy
    fields='__all__'
    #success_url=reverse_lazy('blog-home')
    
    def form_valid(self,form):
        return super().form_valid(form)


    
#class VacancyDeleteView(LoginRequiredMixin,DeleteView):
    #model=Vacancy
    #success_url='/'
