from django import forms
from app1.models import create




class courseForm(forms.ModelForm):
    class Meta:
        model= create
        fields = '__all__'
        labels = {
            'sname':'STUDENT',
            'subject':'SUBJECT',
            'fee':'FEE',
        }
