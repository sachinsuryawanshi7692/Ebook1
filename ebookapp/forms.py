from django import forms
from ebookapp.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmpForm(forms.Form):
    name=forms.CharField(max_length=50)
    dept=forms.CharField(max_length=40)
    email=forms.EmailField(max_length=100)
    salary=forms.FloatField()

class ProductModelForm(forms.ModelForm):
    name=forms.CharField(max_length=60)
    cat=forms.IntegerField()
    price=forms.FloatField()
    status=forms.BooleanField()
    eimage=forms.ImageField()

    class Meta:
        model=Product
        fields=['name','cat']


class UserForm(UserCreationForm):
      
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']


