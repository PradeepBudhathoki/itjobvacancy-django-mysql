from django.urls import path
from .views import  VacancyDetailView,VacancyCreateView,VacancyUpdateView
#from .views import  VacancyListView,VacancyDetailView,VacancyCreateView,VacancyUpdateView

from . import views #import all from views

urlpatterns=[
    path('', views.vacancy_list,name='vacancylist'),
    path('search/',views.vacancy_search,name='vacancy-search'),
    #path('', views.VacancyListView.as_view(),name='vacancy-list'),
    path('<int:pk>/',VacancyDetailView.as_view(),name="vacancy-detail"),
    path('vacancy/new/',VacancyCreateView.as_view(),name="vacancy-create"),
    path('vacancy/<int:pk>/update/',VacancyUpdateView.as_view(),name="vacancy-update"),
    path('vacancy/<int:pk>/delete/',views.vacancy_delete,name="vacancy-delete"),
    #path('<int:pk>/', views.vacancy_detail,name='vacancy-detail'), # get and post req. for update operation
    
]