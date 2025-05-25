from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializer import carSerializer , expenseSeriazlizer ,incomeSerializer
from rest_framework.views import APIView
from .models import Car ,Expense,Income

class CarListCreateAPIView(APIView):
    def get(self,request):
        cars = Car.objects.all()
        serializer = carSerializer(cars,many=True)
        return Response(serializer.data)
    
    def post(self,request):
         serializer = carSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
             
class carDetailAPIView(APIView):
    
    def get (self,request,pk):
        car = get_object_or_404(Car, pk=pk)
        serializer = carSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put (self, request,pk):
        car = get_object_or_404(Car,pk=pk)
        serializer = carSerializer(car,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)        
        return Response({"message":"this car is not found"},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        car = get_object_or_404(Car,pk=pk)
        car.delete()
        return Response({"message":"car delted"},status=status.HTTP_204_NO_CONTENT)
            
        

class expenseCreateListAPIView(APIView):
    def get(self,request):
        expenses = Expense.objects.all()
        serializer = expenseSeriazlizer(expenses,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = expenseSeriazlizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({"mesage":"invalid"},status=status.HTTP_400_BAD_REQUEST)

class expenseDetailsAPIView(APIView):
    def get(self,request,pk):
        expense = get_object_or_404(Expense,pk=pk)
        serializer = expenseSeriazlizer(expense)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put (self,request,pk):
        expense = get_object_or_404(Expense,pk=pk)
        serializer = expenseSeriazlizer(expense,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        expense = get_object_or_404(Expense,pk=pk)
        expense.delete()
        return Response({"message":"item deleted"},status=status.HTTP_204_NO_CONTENT)