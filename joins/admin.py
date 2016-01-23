from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Join

class JoinAdmin(admin.ModelAdmin):
    list_display = ['__str__','email', 'timestamp', 'updated']
    class Meta:
        model = Join

admin.site.register(Join, JoinAdmin)