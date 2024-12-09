from django.shortcuts import render
from .models import TodoList, Category


# # Adding data to the database
# category = Category(name="Work")
# category.save()
# category = Category(name="School")
# category.save()
# category = Category(name="Home")
# category.save()

# todo = TodoList(category=Category.objects.get(name="Work"), task="Do homework", completed=False)
# todo.save()

# Create your views here.

def index(request):
    return render(request, "Todo/index.html")
