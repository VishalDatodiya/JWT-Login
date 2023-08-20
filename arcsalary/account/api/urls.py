
from django.urls import path
from account.api import views

urlpatterns = [
    path('api/login/',views.UserLogin.as_view(), name="login"),
]
