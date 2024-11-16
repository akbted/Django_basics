from django.shortcuts import render
from django.http import HttpResponse
from .models import Todolist, Todoitem

# Create your views here.


def index(reuqest, id):
    ls = Todolist.objects.get(id=id)
    item = ls.todoitem_set.get(id=1)
    return HttpResponse(f"<h1>{ls.name}</h1>")


# Keep in mind the id = 3 because we have only one list in the database and its id is 3. 1 and 2 I deleted them.
