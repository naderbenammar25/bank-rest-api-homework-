from django.urls import path
from . import views

urlpatterns = [
    path('', views.TransactionListCreateAPIView.as_view(), name='transaction-list-create'),
    path('<int:pk>/', views.TransactionRetrieveUpdateDestroyAPIView.as_view(), name='transaction-detail'),
]