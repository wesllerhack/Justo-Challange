from django.db import models


class Employees(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=20)
    isAdmin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    review = models.CharField(max_length=255)
    id_employees = models.ForeignKey(Employees, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class AssignReview(models.Model):
    id_employees = models.ForeignKey(Employees, on_delete=models.CASCADE)
    id_review = models.ForeignKey(Review, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=255, null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
