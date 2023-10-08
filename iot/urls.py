# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Sensor URLs
    path('api/sensors/', views.SensorListCreateView.as_view(), name='sensor-list-create'),
    path('api/sensors/<int:pk>/', views.SensorRetrieveUpdateDestroyView.as_view(), name='sensor-detail'),

    # Reading URLs
    path('api/readings/', views.ReadingListCreateView.as_view(), name='reading-list-create'),
    path('api/readings/<int:pk>/', views.ReadingRetrieveUpdateDestroyView.as_view(), name='reading-detail'),
]
