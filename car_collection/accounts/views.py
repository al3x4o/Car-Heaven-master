from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, render
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .forms import SignUpForm, SignInForm
from django.contrib.auth import views as auth_views, get_user_model
from django.views import generic as views

from .models import Profile

UserModel = get_user_model()


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('signin')

    def form_valid(self, form):
        self.object = form.save()  # The password will be automatically hashed
        # Perform additional actions if needed
        return super().form_valid(form)


class SignInView(LoginView):
    form_class = SignInForm
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('index')

    # Customize the success URL after sign-in


class LogoutUserView(auth_views.LogoutView):
    success_url = '/'


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile-details-page.html'


class ProfileEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = Profile
    success_url = reverse_lazy('index')
    queryset = Profile.objects.all()
    fields = ['username', 'first_name', 'last_name', 'email', 'age', 'profile_picture']

    def get_queryset(self):
        return Profile.objects.all()


class ProfileDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = Profile
    success_url = reverse_lazy('index')
    queryset = Profile.objects.all()
    fields = ['username','first_name', 'last_name', 'email', 'age', 'profile_picture']

    def get_queryset(self):
        return Profile.objects.all()
