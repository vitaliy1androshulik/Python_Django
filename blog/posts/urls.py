
from django.urls import path
from . import views

app_name ="posts"

urlpatterns = [
    path('',views.post_list, name="list"),
    path('create', views.post_new, name="create"),
]
#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
