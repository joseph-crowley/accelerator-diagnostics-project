from django.urls import path

from .views import (
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
    HomeView,
    AboutView,
    PrivacyPolicyView,
)

urlpatterns = [
    # site urls
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),

    # user urls
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

    # admin urls
    path('privacy/', PrivacyPolicyView.as_view(), name='privacy'),
]