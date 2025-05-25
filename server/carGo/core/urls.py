
from django.urls import path
from .views import CarListCreateAPIView,carDetailAPIView,expenseCreateListAPIView,expenseDetailsAPIView

urlpatterns = [
    path("car/",CarListCreateAPIView.as_view()),
    path("cars/<int:pk>/",carDetailAPIView.as_view()),    
    
    path("expense/",expenseCreateListAPIView.as_view()),
    path("expense/<int:pk>/",expenseDetailsAPIView.as_view())
        
]
