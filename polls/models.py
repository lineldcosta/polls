from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
	question_text = models.CharField(max_length = 200)
	pub_date	= models.DateTimeField('Date Published')
	
	def __str__(self):
		return self.question_text
		
	def waspublishedinlast7days(self):
		return self.pub_date >= timezone.now()-datetime.timedelta(days =7)
		
	waspublishedinlast7days.admin_order_field ="pub_date"
	waspublishedinlast7days.boolean ='TRUE'
	waspublishedinlast7days.short_description ='Is published this week?'
	
class Choice(models.Model):
	choice_text	= models.CharField(max_length =200);
	votes	=	models.IntegerField(default = 0)
	question	=	models.ForeignKey(Question)
	
	def __str__(self):
		return self.choice_text