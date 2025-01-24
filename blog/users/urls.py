from django.urls import path
from . import views

app_name ="users"

urlpatterns = [
    path('register',views.register_view),
    path('logout',views.logout_view, name="logout")
]