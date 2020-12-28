from django.contrib import admin
from .models import Blog,Article


class DateCreateAdmin(admin.ModelAdmin):
    readonly_fields = (
        "slug",
        "created",
        "updated",
    )


admin.site.register(Blog,DateCreateAdmin)
admin.site.register(Article)
