from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question, Choice

from django.template import loader

# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)




# Detail Page - displays a question text, with no results but with a form to vote.
# def detail(request, question_id):
#     return HttpResponse(f"You're looking at question {question_id}.") 

# def details(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "polls/details.html", {"question": question})



def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/details.html", {"question": question})

'''
404 error - if the question_id does not exist.
'''


# Results Page - displays results for a particular question.
def result(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")


# Vote Action - handles voting for a particular choice in a particular question.
def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")

