from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import SignUpView, SignInView, ProfileEditView, ProfileDeleteView, ProfileDetailsView, LogoutUserView

urlpatterns = [
    # Other URL patterns
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile details'),
        path('edit/', ProfileEditView.as_view(), name='profile edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile delete'),
        path('logout/', LogoutUserView.as_view(), name='profile logout'),
    ]))
]
