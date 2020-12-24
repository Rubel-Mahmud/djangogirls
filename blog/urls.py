from django.urls import path
from blog.views import *
urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:pk>/remove/', post_remove, name='post_remove'),
    path('post/drafts/', post_draft, name='post_drafts'),
    path('post/<int:pk>/approve/', post_approve, name='post_approve'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
    path('post/<int:pk>/comment/', post_comment, name='post_comment'),
]