
from django.urls import path
from . import views

app_name ="posts"

urlpatterns = [
    path('',views.post_list),
]
#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
