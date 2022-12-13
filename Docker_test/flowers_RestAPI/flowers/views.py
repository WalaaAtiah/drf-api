from django.shortcuts import render

from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import FlowerSerializer
# Create your views here.
from .models import Flower


class FlowerListView(ListCreateAPIView):
    queryset=Flower.objects.all()
    serializer_class= FlowerSerializer

#serializer_class: use to create file to convert python file to json formate
# all the models convert it to json file

class FlowerDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Flower.objects.all()
    serializer_class= FlowerSerializer
