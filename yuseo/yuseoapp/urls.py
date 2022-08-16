from unicodedata import name
from django import views
from django.urls import include, path

from .views import UploadView, YuseoDetail, Yuseo

urlpatterns = [
    path('yuseo/', Yuseo.as_view()),
    path('yuseo/<int:pk>', YuseoDetail.as_view()),
    path('upload/', UploadView.as_view(), name="file_upload")
]
