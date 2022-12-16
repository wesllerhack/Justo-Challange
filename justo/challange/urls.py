from django.urls import path

from .views import EmployeesApiView, ReviewApiView, AssignReviewApiView


urlpatterns = [
  path('employees/', EmployeesApiView.as_view(), name='employees'),
  path('review/', ReviewApiView.as_view(), name='review'),
  path('assignreview/', AssignReviewApiView.as_view(), name='assignreview')

]