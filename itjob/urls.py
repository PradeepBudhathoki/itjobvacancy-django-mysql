from django.urls import path
from .views import VacancyListView, VacancyDetailView,VacancyCreateView,VacancyDeleteView,VacancyUpdateView

from . import views #import all from views

urlpatterns=[
    
    path('', views.VacancyListView.as_view(),name='itjob-list'),
    path('<int:pk>/',VacancyDetailView.as_view(),name="itjob-detail"),
    path('vacancy/new/',VacancyCreateView.as_view(),name="vacancy-create"),
    path('vacancy/<int:pk>/update/',VacancyUpdateView.as_view(),name="vacancy-update"),
    path('vacancy/<int:pk>/delete/',VacancyDeleteView.as_view(),name="vacancy-delete"),
    #path('<int:pk>/', views.vacancy_detail,name='vacancy-detail'), # get and post req. for update operation
    #path('delete/<int:id>/',views.vacancy_delete,name='vacancy_delete')

]