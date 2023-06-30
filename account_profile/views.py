from typing import Any
from django import http
from django.shortcuts import render
from django.views.generic import TemplateView
# from .forms import UserProfileForm




class accountView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'account_profile/account.html', {})
    


# class profileView(TemplateView):
    
#         # model = UserProfile
#         # form = UserProfileForm()
#         template_name = 'account_profile/profile.html'
        
#         def get(self, request, *args, **kwargs):
#              return super().get(request, *args, **kwargs)
    


    # def profile_form(request):
    # form = UserProfileForm()
    
    #     return render(request, 'account_profile.html', {'form': form})
        
    

# class loginView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'account_profile/login.html', {})
    
    
# class registrationView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'account_profile/registration.html', {})
    
    
        
    

