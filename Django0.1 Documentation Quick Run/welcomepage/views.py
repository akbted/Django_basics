from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#FBV - Function Based View
def welcome_page(request):
    user_name = "John Doe"
    context = {
        "user_name": user_name
    }
    return render(request, 'welcomepage.html', context)

