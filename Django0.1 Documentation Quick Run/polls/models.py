from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200) # CharField is used for character fields amd it is used in Validation as well.
    pub_date = models.DateTimeField("date published")

    # Defining a method to check if the question was published recently or not.
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timezone.timedelta(days = 1) # timedelta is used to calculate the difference between two dates.

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # ForeignKey is used to create a relationship between two tables.
    choice = models.CharField(max_length=200)
    vote = models.IntegerField(default=0) # IntegerField is used for integer fields.

    def __str__(self):
        return self.choice