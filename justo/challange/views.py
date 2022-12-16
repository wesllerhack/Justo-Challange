from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Employees, Review, AssignReview
from .serializers import EmployeesSerializer, ReviewSerializer, AssignReviewSerializer

class EmployeesApiView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    employees = Employees.objects.all()
    serializer = EmployeesSerializer(employees, many=True)
    return Response(serializer.data)

  def post(self, request):
    employees = EmployeesSerializer(data=request.data)
    employees.is_valid(raise_exception=True)
    employees.save()
    return Response(employees.data, status=status.HTTP_201_CREATED)

class ReviewApiView(APIView):

  def get(self, request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True)
    return Response(serializer.data)

    

class AssignReviewApiView(APIView):

  def get(self, request):
    review = AssignReview.objects.all()
    serializer = AssignReviewSerializer(review, many=True)
    return Response(serializer.data)

