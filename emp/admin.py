from django.contrib import admin
from .models import emp,Testimonial
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','empid','phone')
    list_editable=('working','empid')
    search_fields=('name','phone')
    list_filter=('working',)

admin.site.register(emp,EmpAdmin)
admin.site.register(Testimonial)