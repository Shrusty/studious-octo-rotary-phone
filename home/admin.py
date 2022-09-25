import imp
from django.contrib import admin

# Register your models here.
from home.models import Contact
from home.models import Post


admin.site.register(Contact)
admin.site.register(Post)