from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories" # This is used to change the name of the table in the admin panel.

class TodoList(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks') # This is used to create a foreign key relationship between the Category and TodoList models. # Related name is used to access the tasks of a category.
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
    
    class Meta:
        ordering = ['created'] # This is used to order the tasks based on the created field.

