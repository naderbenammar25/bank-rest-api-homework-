from django.urls import path
from .views import ClientListCreateAPIView, ClientRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('clients/', ClientListCreateAPIView.as_view(), name='client_list_create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view(), name='client_retrieve_update_destroy'),
]
