from django.contrib import admin
from .models import Note, Trait, Wine, Winery

admin.site.register(Note)
admin.site.register(Trait)
admin.site.register(Wine)
admin.site.register(Winery)