from django.urls import path

# from .views import RegisterList, CheckEmail
from .views import RegisterList

app_name = "register"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('register/', RegisterList.as_view()),
    # path('check/', CheckEmail.as_view()),
]
