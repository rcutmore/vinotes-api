from django.contrib import admin
from .models import Note, Wine, Winery

admin.site.register(Note)
admin.site.register(Wine)
admin.site.register(Winery)