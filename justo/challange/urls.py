from django.urls import path

from .views import EmployeesApiView, ReviewApiView, AssignReviewApiView


urlpatterns = [
  path('employees/', EmployeesApiView.as_view(), name='employees')
]