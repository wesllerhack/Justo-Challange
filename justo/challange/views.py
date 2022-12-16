from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Employees, Review, AssignReview
from .serializers import EmployeesSerializer, ReviewSerializer, AssignReviewSerializer

class EmployeesApiView(APIView):

  def get(self, request):
    employees = Employees.objects.all()
    serializer = EmployeesSerializer(employees, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = EmployeesSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

  def delete(self, request):
    employees = Employees.objects.all()
    employees.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewApiView(APIView):

  def get(self, request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = ReviewSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

class AssignReviewApiView(APIView):

  def get(self, request):
    assignreview = AssignReview.objects.all()
    serializer = AssignReviewSerializer(assignreview, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = AssignReviewSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

