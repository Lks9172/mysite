from django.contrib import admin
from .models import Book,Wisesaying
# Register your models here.

admin.site.site_title="running water"
admin.site.site_header="first django"

class WisesayingInline(admin.StackedInline):
    model = Wisesaying

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name','author','instroduce')
    inlines = [WisesayingInline]
    fieldsets = [
    ('Book Name', {'fields': ['name','author']}),
    ('instroduce', {'fields': ['instroduce']}),
    ]
