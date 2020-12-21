from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import VacancyForm
from .models import Vacancy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def vacancy_list(request):
    context={
        'vacancys':Vacancy.objects.all()
    }
    return render(request,"itjob/vacancy_list.html",context)



class VacancyListView(ListView):
    paginate_by =3
    model=Vacancy#what model to query;posts
    template_name='itjob/vacancy_list.html'#<app>/post_list.html
    context_object_name='vacancys'
    ordering=['-published_date'] #-sign indicates newest to oldest


class VacancyDetailView(DetailView):
    model=Vacancy
    
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

class VacancyDeleteView(LoginRequiredMixin,DeleteView):
    model=Vacancy
    success_url='/'
