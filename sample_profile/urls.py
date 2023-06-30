
from django.urls import path, include
from sample_profile.views import PreviewView, FeaturesView, LoginView, RegistrationView, CreateProfileView, ProfileView, LogoutView

app_name = 'sample_profile'

urlpatterns = [
    path('', PreviewView.as_view(), name='home'),
    path('features/', FeaturesView.as_view(), name='features'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('create_profile/', CreateProfileView.as_view(), name='create_profile'),
    path('profile/', ProfileView.as_view(), name='profile'),
    # path('profile/<str:user_name>', ProfileView.as_view(), name='profile'),
    path('logout', LogoutView.as_view(), name='logout')
      
]