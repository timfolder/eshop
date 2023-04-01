from django.urls import path
from .views import GalleryPage, ChairPage, ChairCreatePage


urlpatterns = [
    path('', GalleryPage.as_view(), name='gallery'),
    path('create/', ChairCreatePage.as_view(), name='chaireation'),
    path('<slug:slug>/', ChairPage.as_view(), name='chair_details'),
]