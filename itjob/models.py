from django.db import models
from django.utils import timezone
from PIL import Image
from django.urls import reverse
from django.contrib.auth.models import User

class Skill(models.Model):
    skill_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    category_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    skill=models.ForeignKey(Skill,models.DO_NOTHING)

    def __str__(self):
        return self.name



class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,blank=False,null=False)
    image=models.ImageField(default='default.jpg', upload_to='company_pics')
    address = models.CharField(max_length=20)
    phone= models.CharField(max_length=15,blank=False,null=False)
    email= models.CharField(max_length=20,null=False)
    description=models.TextField()

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    vacancy_id=models.AutoField(primary_key=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    skill=models.ForeignKey(Skill,models.DO_NOTHING)
    category=models.ForeignKey(Category,models.DO_NOTHING)
    title = models.CharField(max_length=100)
    published_date = models.DateField(default=timezone.now)
    apply_before= models.DateField(null=True)
    req_no=models.IntegerField(null=True)
    salary=models.CharField(max_length=10,null=True)
    education=models.CharField(max_length=60,null=True)
    requirements=models.TextField(null=True)

    

    def __str__(self):
        return self.title


    def get_absolute_url(self):      
        return reverse('vacancy-detail', kwargs={'pk':self.vacancy_id})
