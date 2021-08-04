from django.contrib import admin
from .models import Comments, Contributors, Projects, Issues

# Register your models here.

admin.site.register(Comments)
admin.site.register(Contributors)
admin.site.register(Projects)
admin.site.register(Issues)
