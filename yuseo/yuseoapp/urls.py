from django.urls import path
from .views import YuseoDetail, YuseoList

urlpatterns = [
    path('yuseo/', YuseoList.as_view()),
    path('yuseo/<int:pk>', YuseoDetail.as_view()),
]
