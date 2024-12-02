from django.urls import path
from .views import RegisterView, ManagePreferencesView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('preferences/', ManagePreferencesView.as_view(), name='manage-preferences'),
    path('logout/', LogoutView.as_view(), name='logout')
]