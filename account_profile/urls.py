from django.urls import path, include
from django.views.generic.base import TemplateView

from account_profile.views import accountView

app_name = 'account_profile'

urlpatterns = [
    
    # path('profile/', profileView.as_view(), name='profile'),
    # path('login/', loginView.as_view(), name='login'),
    # path('registration/', registrationView.as_view(), name='registration'),
    
]