
from django.urls import path
from . import views

app_name ="posts"

urlpatterns = [
    path('',views.post_list, name="list"),
    path('create', views.post_new, name="create"),
    path('details/<int:post_id>/', views.post_details, name="details"),
    path('delete/<int:post_id>/', views.delete_post, name='delete'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]
#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
