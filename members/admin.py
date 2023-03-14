from django.contrib import admin

from . models import *

class MemberAdmin(admin.ModelAdmin):
    list_display=('firstname','lastname','joined_date')
admin.site.register(Member, MemberAdmin)

# Register your models here.
