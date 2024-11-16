# Keep in mind the id = 3 because we have only one list in the database and its id is 3. 1 and 2 I deleted them.


from django.shortcuts import render
from django.http import HttpResponse
from .models import Todolist, Todoitem

# Create your views here.


def index(request, id):
    try:
        ls = Todolist.objects.get(id=id)
    except Todolist.DoesNotExist:
        return HttpResponse(f"<h1>Todolist with id {id} does not exist.</h1>")

    items = ls.todoitem_set.all()
    if not items:
        return HttpResponse(f"<h1>No Todoitems in Todolist {ls.name}.</h1>")

    items_text = ", ".join([item.text for item in items])
    return HttpResponse(f"<h1>{ls.name}: {items_text}</h1>")
