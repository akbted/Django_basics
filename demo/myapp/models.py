from django.db import models

# Create your models here.
# We can create Database mode here
# ORM - we can write python code to create Databases in Django using Object Relation Mapping


# Model to create a simple Database of TodoItems
class TodoItem(models.Model):
    title = models.CharField(max_length=200)  # Char Field
    description = models.TextField()
    completed = models.BooleanField(default=False)  # Boolean Field
