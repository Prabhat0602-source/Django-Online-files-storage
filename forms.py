from django import forms
from .models import userdata

class loginpage(forms.Form):
    un = forms.CharField(max_length = 30)
    pa = forms.CharField(max_length = 30)


class clgdata(forms.Form):
   enrollnment= forms.CharField(max_length = 30)
   branch = forms.CharField(max_length = 30)
   year = forms.CharField(max_length = 30)

class subdata(forms.Form)  :
    subject1=forms.CharField(max_length=30,required=False)
    subject2=forms.CharField(max_length=30,required=False)
    subject3=forms.CharField(max_length=30,required=False)
    subject4=forms.CharField(max_length=30,required=False)
    subject5=forms.CharField(max_length=30,required=False)
    subject6=forms.CharField(max_length=30,required=False)
    subject7=forms.CharField(max_length=30,required=False)
    subject8=forms.CharField(max_length=30,required=False)
class change(forms.Form):
    pc=forms.CharField(max_length=30)
class ppchange(forms.Form):
    passi=forms.CharField(max_length=30)
class GeeksForm(forms.Form):
    Choose_File= forms.FileField()

class delete(forms.Form):
    dele=forms.CharField(max_length = 1000)

class userdata(forms.ModelForm):
	class Meta:
		model 	= userdata
		fields 	=	[
			'username',
			'password',
			'email',
			'phonenumber',
            #'clgdata',
            #'subdata',
            'branch',
            'year',
            'enrollnment',
            'subject1',
            'subject2',
            'subject3',
            'subject4',
            'subject5',
            'subject6',
            'subject7',
            'subject8',

		]
