from django.contrib import admin
from .models import Word, Rhymes

class RhymesAdmin(admin.TabularInline):
    model = Rhymes
    extra = 3

class WordAdmin(admin.ModelAdmin):
    inlines = [RhymesAdmin]
    list_display = ['unstressed_word', 'all_stresses', 'stressed_word']
    search_fields = ['unstressed_word']


admin.site.register(Word, WordAdmin)
