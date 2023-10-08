from rest_framework import generics
from .models import Fire
from .serializers import FireSerializer

class FireListCreateView(generics.ListCreateAPIView):
    queryset = Fire.objects.all()
    serializer_class = FireSerializer

class FireRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fire.objects.all()
    serializer_class = FireSerializer
