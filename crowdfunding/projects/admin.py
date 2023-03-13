from django.contrib import admin
from .models import Project
from .models import Pledge

admin.site.register(Project)

admin.site.register(Pledge)
