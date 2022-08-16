from unicodedata import name
from django import views
from django.urls import include, path

from .views import UploadView, YuseoDetail, Yuseo, YuseoOne,YuseoTwo

urlpatterns = [
    path('yuseo1/', YuseoOne.as_view()),
    path('yuseo2/', YuseoTwo.as_view()),
    path('yuseo/<int:pk>', YuseoDetail.as_view()),
    path('upload/', UploadView.as_view(), name="file_upload"),
]
