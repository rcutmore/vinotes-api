from django.contrib import admin
from .models import Note, Trait, Wine, Winery

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    filter_horizontal = (
        'color_traits',
        'nose_traits',
        'taste_traits',
        'finish_traits',
    )

admin.site.register(Trait)
admin.site.register(Wine)
admin.site.register(Winery)