from django.urls import path

from . import views


# ใในใ็จ
urlpatterns = [
    path('followings/<int:user_id>', views.followings.as_view(), name='followings'),
    path('followers/<int:user_id>', views.followers.as_view(), name='followers'),
]

