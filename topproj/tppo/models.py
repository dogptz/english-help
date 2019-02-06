from django.db import models

# Create your models here.

class theory(models.Model):

	name = models.CharField(max_length=20)
	text = models.TextField() 

class users(models.Model):
	name = models.CharField(max_length=20)
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