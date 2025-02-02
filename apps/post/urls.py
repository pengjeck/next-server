from django.urls import path
from apps.post import views as user_views

urlpatterns = [
    path('post', user_views.get_post_list, name = 'get_post_list'),
    path('post/<int:post_id>', user_views.get_post_by_id, name = 'get_post_by_id'),
    path('/manage/post/<int:post_id>', user_views.update_post, name = 'update_post')
]