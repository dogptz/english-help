from django.db import models
from django import forms


# Create your models here.

class theme_new(models.Model):

	theme_name = models.TextField()

class grammar(models.Model):

	name = models.TextField()
	text = models.TextField()


class theory(models.Model):

	name = models.CharField(max_length=20)
	text = models.TextField() 

class users(models.Model):
	user = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

class Question(models.Model):
	"""docstring for Question"""
	question_text = models.CharField(max_length=200)
	def __str__(self):
		return self.question_text

class Choice(models.Model):
	"""docstring for ClassName"""
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	stat = models.BooleanField(default=False)
	poper = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text



