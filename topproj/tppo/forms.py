from django import forms
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

def valid_reg(value):
	print (value)
	print(ValidationError,"a")
	if value == "1":	
		raise ValidationError("Всё хуйня")
		
	


def valid_pass(value):
	if value == "1":
		raise ValidationError("Всё хуйня с паролем")
	

class Registration(forms.Form):
	login = forms.CharField(validators=[valid_reg])
	password = forms.CharField(validators=[valid_pass])


