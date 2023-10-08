from django.urls import path
from . import views

urlpatterns = [
    path('api/fires/', views.FireListCreateView.as_view(), name='fire-list-create'),
    path('api/fires/<int:pk>/', views.FireRetrieveUpdateDestroyView.as_view(), name='fire-detail'),
]
