from django.urls import path
from .views import FlowerListView,FlowerDetailView

urlpatterns = [
   path('', FlowerListView.as_view(), name='flower_list'),
   path('<int:pk>', FlowerDetailView.as_view(),name='flower_detail')
]
