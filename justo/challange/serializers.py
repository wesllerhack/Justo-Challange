from rest_framework import serializers
from justo.challange import models


class EmployeesSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Employees
    fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Review
    fields = '__all__'

class AssignReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.AssignReview
    fields = '__all__'