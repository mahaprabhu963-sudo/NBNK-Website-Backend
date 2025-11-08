from django.urls import path
from .views import login_user
from .views import logout
from . import views




from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView
)

urlpatterns = [
    path('register/', views.sign_in, name="sign_in"),
    path('current_user/', views.current_user, name="current_user"),
    path('logout/', views.logout, name='logout'),
    path('log_in/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', views.login_user, name='login_user'),

]