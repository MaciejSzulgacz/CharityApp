from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView

from .forms import CustomUserLoginForm, CustomUserRegisterForm
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
    form_class = CustomUserRegisterForm
    template_name = "charity/register.html"

    def form_valid(self, form):
        cd = form.cleaned_data
        email = cd['email']
        password = cd['password']
        name = cd['name']
        surname = cd['surname']
        CustomUser.objects.create_user(email=email, password=password, name=name, surname=surname)
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
        bags = request.POST.get('bags')
        category_id = request.POST.get('categories')
        organization_id = request.POST.get('organization')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        postcode = request.POST.get('postcode')
        date = request.POST.get('date')
        time = request.POST.get('time')
        comments = request.POST.get('comments')
        category = Category.objects.get(id=category_id)
        organization = Institution.objects.get(id=organization_id)
        new_donation = Donation.objects.create(quantity=bags, institution=organization, address=address,
                                               phone_number=phone, city=city, zip_code=postcode, pick_up_date=date,
                                               pick_up_time=time, pick_up_comment=comments)
        new_donation.categories.add(category)
        new_donation.save()
        return redirect('form-confirmation')


class ProfilView(View):
    template_name = "charity/profil.html"

    def get(self, request):
        current_user = request.user
        return render(request, self.template_name, {"current_user": current_user})


class FormConfirmationView(View):
    template_name = "charity/form-confirmation.html"

    def get(self, request):
        current_user = request.user
        return render(request, self.template_name, {"current_user": current_user})
