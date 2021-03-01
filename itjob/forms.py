from django import forms 
from .models import Vacancy

class VacancyForm(forms.ModelForm):
    
    class Meta:
        model=Vacancy
        fields='__all__'
        labels={
            'title':'Job Title',
            'vacancy_id':'Vacancy ID',
            'company':'Company Name',
            'category':'Category',
            'req_no':'Required No.',
            'salary':'Salary',
            'education':'Education',
            'pulished_date':'Published Date',
            'apply_before':'Deadline',
            'requirements':'Requirements',
            'skill':'Skills Required'
        }

    def __init__(self, *args, **kwargs):
        super(VacancyForm,self).__init__(*args, **kwargs)
        self.fields['company'].empty_label = "" #for displaying select instead of ...
        self.fields['skill'].empty_label = "Select"
        