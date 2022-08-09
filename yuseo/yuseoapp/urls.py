from unicodedata import name
from django import views
from django.urls import include, path

from .views import UploadView, YuseoDetail, YuseoList

urlpatterns = [
    path('yuseo/', YuseoList.as_view()),
    path('yuseo/<int:pk>', YuseoDetail.as_view()),
    path('upload/', UploadView.as_view(), name="file_upload")
]
