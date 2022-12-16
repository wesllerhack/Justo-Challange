from django.contrib import admin

from .models import Employees, Review, AssignReview

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
  list_display = ('name', 'user', 'password', 'isAdmin', 'created_at', 'updated_at')
