from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView

from .forms import CustomUserLoginForm
from .models import Category, CustomUser, Donation, Institution


class LoginView(FormView):
    form_class = CustomUserLoginForm
    template_name = "charity/login.html"

    def form_valid(self, form):
        cd = form.cleaned_data
        email = cd['email']
        password = cd['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('landing_page')
        return redirect('login')


class RegisterView(FormView):
    form_class = CustomUserLoginForm
    template_name = "charity/register.html"

    def form_valid(self, form):
        cd = form.cleaned_data
        email = cd['email']
        password = cd['password']
        CustomUser.objects.create_user(email=email, password=password)
        return redirect('login')


class LandingPageView(View):
    template_name = "charity/index.html"

    def get(self, request):
        donations = Donation.objects.all()
        institutions = Institution.objects.all()
        quantity = 0
        sum_of_institutions = 0
        for donation in donations:
            quantity += donation.quantity
        for _ in institutions:
            sum_of_institutions += 1
        return render(request, self.template_name, {"quantity": quantity,
                                                    "sum_of_institutions": sum_of_institutions,
                                                    "institutions": institutions})


class LogoutView(View):
    template_name = "charity/index.html"

    def get(self, request):
        logout(request)
        return render(request, self.template_name)


class AddDonationView(View):
    template_name = "charity/form.html"

    def get(self, request):
        current_user = request.user
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, self.template_name, {"current_user": current_user,
                                                    "categories": categories,
                                                    "institutions": institutions})

    def post(self, request):
        print(">>>>>>>>>")
        name = request.POST.get('categories')
        street = request.POST.get('address')
        city = request.POST.get('city')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        print(city)
        print(phone)
        print(">>>>>>>>>")
        return render(request, self.template_name, {"name": name,
                                                    "address": street,
                                                    "city": city,
                                                    "postcode": postcode,
                                                    "phone": phone})


class ProfilView(View):
    template_name = "charity/profil.html"

    def get(self, request):
        current_user = request.user
        return render(request, self.template_name, {"current_user": current_user})
