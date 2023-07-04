from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .forms import CreateUserForm, CreateProfileForm

from .models import Profile

class PreviewView(TemplateView):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'sample_profile/sample.html', {})
    
class FeaturesView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'sample_profile/features.html', {})    
    
def not_logged_in(user):
    return not user.is_authenticated

# @user_passes_test(not_logged_in, login_url='/sample_profile/profile/')

class LoginView(LoginView):
        
    template_name = 'registration/login.html'
    authentication_form = AuthenticationForm
    success_url = reverse_lazy('sample_profile/profile/')
    
    redirect_authenticated_user = True
    
    # def form_valid(self, form):
    #     response = super().form_valid(form)
        # messages = messages.success(self.request, 'You are now logged in')
        # return response
    
    # def form_valid(self, request):
        # self.request is redundant because LoginView already has a request attribute 
        # if request.method == 'POST':         
        #     form = CreateUserForm
        #     username = request.POST.get('username')               
        #     password = request.POST.get('password')       
                   
        #     user = authenticate(username=username, password=password)
            
        #     if user is not None:
        #         login(self.request, user)
        #         return redirect('sample_profile:profile')
            # else:
            #     messages.info(self.request, 'Username or password is incorrect')
            #     return self.form_invalid(form)
              
class RegistrationView(FormView):
    
    template_name = 'registration/register.html'
    form_class = CreateUserForm
    success_url = '/sample_profile/profile/'
    
    def form_valid(self, form):
        if self.request.method == 'POST':
            form = CreateUserForm(self.request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(self.request, 'Account created successfully for' + user)
                
        return super().form_valid(form)
    
    #CBV does not need this method unless im adding logic to GET request
    # def get(self, request, *args, **kwargs):
    #     form = CreateUserForm()
        
    #     if request.method == 'POST':
    #         form = CreateUserForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('sample_profile:overview')
        
    #     context = {'form': form}
    #     return render(request, 'registration/register.html', context)
    
class CreateProfileView(FormView):
    
    template_name = 'sample_profile/create_profile.html'
    form_class = CreateProfileForm
    success_url = '/sample_profile/profile/'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["user"] = user
        
        print( 'user: ', user)
        return context
        
    def form_valid(self, form):
               
        profile = form.save()
        print('profile: ', profile)
        
        profile.user = form.cleaned_data.get('user')
        
        print('profile.user: ', profile.user)
        
        profile.save()
        
        return super().form_valid(form)
        
        # form.instance.user = self.request.user    
        # return super().form_valid(form)
    
class ProfileView(TemplateView):
   
    model = Profile
    template_name = 'sample_profile/profile.html'
    context_object_name = 'profiles'
    
    
    # def get(self, request):
    #     user_profile = Profile.objects.get(user=request.user)
    #     context = {'user_profile': user_profile}
    #     context = {}
    #     return render(request, self.template_name, context)
    
    # def get_object(self, queryset=None):
    #     return self.request.user.profile
   
class LogoutView(TemplateView):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('sample_profile:login')
