from django import forms
from django.forms import ModelForm
from .models import Students

class StudentForm(ModelForm):
    class Meta:
 
        model = Students
        fields = ('index' , 'f_name' , 'l_name' , 'email' , 'department')

          

        labels ={'index': "",
                'f_name': '',
                'l_name': '',
                'email' : '',
                'department': '',
                  } 

        widgets = {'index': forms.TextInput(attrs={'class':'form-control','placeholder':'Index No'}) ,
                  'f_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}) ,
                  'l_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}) ,
                  'email' : forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}) ,
                  'department': forms.Select(attrs={'class': 'form-control'}),
                  }
        
StudentForm(initial={'department': 'option2'})
       
        