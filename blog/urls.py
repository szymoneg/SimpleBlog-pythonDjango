from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.serve_test, name='index'),
    path('getAll/', views.get_all_posts, name='getAll'),
    path('addNew', views.add_new_post, name='addNew'),
    path('updatePost/<int:id_post>', views.update_post, name='updatePost')
]
