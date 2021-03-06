from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import theory
from .models import users , Question, Choice
from django.shortcuts import get_object_or_404
from .forms import UserForm
from django.urls import reverse
from django.views import generic



# Create your views here.
def first(request):
	test = get_object_or_404(theory, id=1)
	return render(request,"first.html", {"text": test})

def two(request, num):
	test = get_object_or_404(theory, id=num)
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

   