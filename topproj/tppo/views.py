from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import theory, theme_new, grammar
from .models import users , Question, Choice
from django.shortcuts import get_object_or_404
from .forms import UserForm, Registration
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth 
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth import base_user
# Create your views here.


def first(request):
	count = theme_new.objects.all()
	return render(request,"first.html", {"count": count})

def two(request, num):
	test = get_object_or_404(theory, id=num)
	return render(request,"two.html", {"text": test})

def grammarpage(request):
	counter = grammar.objects.all()
	return render(request,"grammarpage.html", {"counter": counter})

def grammarpa(request, num):
	test = get_object_or_404(grammar, id=num)
	return render(request,"two.html", {"text": test})

def index(request):
	if request.method == "POST":
		name = request.POST.get("name")
		password = request.POST.get("password")
		name_prof = get_object_or_404(users, name = name)
		if (password == name_prof.password):
			return HttpResponseRedirect('/theme/')
		else:
			userform = UserForm()
			return render(request, "form.html", {"form": userform, "message": "Неверный логин или пароль"})
	else:
		userform = UserForm()
		return render(request, "form.html", {"form": userform})


def regist(request):
	form = UserCreationForm()

	if request.method == "POST":
		form = UserCreationForm(request.POST)
		print (form)
		#if form.is_valid():
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect(" ")
		else:
			kek = User.objects.get(username = request.POST['username'])
			print(kek.username, "kak")
			if request.POST['username'] == kek.username:
				form = UserCreationForm()
				return render(request, "form.html", {"form": form, "message": 'такой есть'})
			else:
				print(request.POST['username'])
				form = UserCreationForm()
				return render(request, "form.html", {"form": form, "message": 'другая ошибка'})
	else:
		form = UserCreationForm()
		return render(request, "form.html", {"form": form})
	
    	

 


def vote(request):
    question = get_object_or_404(Question, pk=1)
    question2 = get_object_or_404(Question, pk=2)
    mark = 0

    try:
    	selected_choice = question.choice_set.get(pk=request.POST['choice'])
    	selected_choice2 = question2.choice_set.get(pk=request.POST['choice2'])
    except (KeyError, Choice.DoesNotExist):
    	return render(request, 'test.html', {"question": question, "question2": question2})
    else:
    	if(selected_choice.poper == 1):
    		mark += 1
    	if(selected_choice2.poper == 1):
    		mark += 1
    	return HttpResponse("<h2>Вы ответили правильно на {0}</h2>".format(mark))

   

def avtoriz(request):
	if request.method == "POST":
		name = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username = name, password = password)
	
		if user is not None and user.is_active:
			auth.login(request, user)
			userform = UserForm()
			return render(request, "form.html", {"form": userform, "message": "нихао"})
	
		else:
			userform = UserForm()
			return render(request, "form.html", {"form": userform})

	else:
		userform = UserForm()
		return render(request, "form.html", {"form": userform})



def logout(request):
	auth.logout(request)
	return HttpResponseRedirect("/account/loggedout/")
