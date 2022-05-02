from django.urls import path
from . import views

# Creating URL Routes for all API views to serve as endpoints
urlpatterns = [
    path("", views.getRoutes, name='routes'),
    path("codes/", views.CodesListCreateAPIView.as_view(), name='codes'), 
    path("codes/<int:id>/", views.CodesDetailAPIView.as_view(), name='getCode'),
    path("codes/<int:id>/delete", views.CodesDeleteAPIView.as_view(), name='deleteCode'),
    path("codes/fileupload", views.CodesUploadAPIView.as_view(), name='fileUpload')
]