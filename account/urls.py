from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # path("", views.user_login, name="user_login")
    path("", views.dashboard, name="dashboard"),
    # path("login/", auth_views.LoginView.as_view(), name="login"),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Change password
#     path("password_change/", auth_views.PasswordChangeView.as_view(),
#          name="password_change"),
#     path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(),
#          name="password_change_done"),

    # Reset password
#     path("password_reset/", auth_views.PasswordResetView.as_view(),
#          name="password_reset"),
#     path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(),
#          name="password_reset_done"),
#     path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(),
#          name="password_reset_confirm"),
#     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
#          name='password_reset_complete'),
     path('', include('django.contrib.auth.urls')),

     path('register/', views.register, name='register'),
     path("edit/", views.edit, name="edit"),

     # Social Auth
     path('social-auth/', include('social_django.urls',namespace='social')),

    #  users page 
    path('users/', views.user_list, name='user_list'),
    # user follow
    path('users/follow/', views.user_follow, name='user_follow'),
    # user profile
    path('users/<username>/', views.user_detial, name='user_detail'),

    
]
