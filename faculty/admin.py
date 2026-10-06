from django.contrib import admin

from .models import Department, Exchange, HomePage, Program, Teacher


@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ("university", "country", "places", "deadline", "status")
    list_filter = ("country", "deadline")
    search_fields = ("university", "country", "description")


admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Teacher)
admin.site.register(HomePage)
