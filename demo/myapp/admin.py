from django.contrib import admin
from .models import TodoItem

# Register your models here.
# After creating the model we have to register the model here - so they can appear in admin pannel so we can modify them.

admin.site.register(TodoItem)

# After we make some changes to the model we need to make a migration.
# Every time we make some changes to model we need  do migration so that the data will still remain however the database will be modified based on new schema.
