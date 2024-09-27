from django.contrib import admin
from MainApp.models import Snippet


# Register your models here.
# 1 вариант
# admin.site.register(Snippet)

# 2 вариант
@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ["name", "lang", "creation_date", "code"]
    list_filter = ["lang", "creation_date"]
    ordering = ["creation_date"]
    search_fields = ["name", "code"]