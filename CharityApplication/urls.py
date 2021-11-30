from django.contrib import admin
from django.urls import path
from charity.views import AddDonationView, FormConfirmationView, LandingPageView, LoginView, LogoutView, ProfileView,\
    RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name="landing_page"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('add_donation/', AddDonationView.as_view(), name="add_donation"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('form-confirmation/', FormConfirmationView.as_view(), name="form-confirmation"),
]
