from django.db import models

# Create your models here.


class Todolist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Todoitem(models.Model):
    todolist = models.ForeignKey(Todolist, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text
