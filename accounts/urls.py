from django.urls import path
from .views import LoginPage, logoutview, RegisterPage

urlpatterns = [
    path('login/', LoginPage.as_view(), name="login"),
    path('logout/', logoutview, name="logout"),
    path('signup/', RegisterPage.as_view(), name="signup" )
]