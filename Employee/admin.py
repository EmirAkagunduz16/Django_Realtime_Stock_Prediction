from django.contrib import admin
from .models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'salary')
    list_filter = ('name', 'email', 'phone', 'address', 'salary')
    search_fields = ('name', 'email', 'phone', 'address', 'salary')

admin.site.register(Employee, EmployeeAdmin)
