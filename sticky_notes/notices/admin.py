from django.contrib import admin
from .models import Notice
from .models import Author
# Register your models here.

# Post model
admin.site.register(Notice)
# Author model
admin.site.register(Author)
