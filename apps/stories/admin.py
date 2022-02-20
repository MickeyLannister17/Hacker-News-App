from django.contrib import admin
from .models import Story, Vote

# Register your models here.
admin.site.register(Story)
admin.site.register(Vote)