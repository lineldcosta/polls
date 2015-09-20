from django.shortcuts import render

from django.http import HttpResponse

from .models import Question, Choice

from django.http import Http404

# Create your views here.
def index(request):
	latest_questions = Question.objects.order_by("-pub_date")[:5];
	print(latest_questions)
	context ={"latest_questions" : latest_questions};
	return render(request, 'polls/index.html', context)
	
def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise http404("Question does not exists")
	else:
		return render(request,'polls/detail.html',{'question' : question}	);
	
def results(request, question_id):
	return HttpResponse("These are the results of hte question %s" % question_id)
	
def vote(request, question_id):
	return HttpResponse("These are the votes of the question %s" % question_id)