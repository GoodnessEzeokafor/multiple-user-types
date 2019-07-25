from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .decorators import buyer_required, seller_required

from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from .forms import SellerSignUpForm,BuyerSignUpForm
from .models import User
# Create your views here.



class BuyerSignupView(CreateView):
    model = User
    form_class = BuyerSignUpForm
    template_name = "buyer/signup.html"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Buyer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user) 
        return redirect('buyer_dashboard')

class SellerSignupView(CreateView):
    model = User
    form_class = SellerSignUpForm
    template_name = "seller/signup.html"

    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Seller'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user) 
        return redirect('seller_dashboard')


@login_required
@buyer_required
def buyer_dashboard(request):
    template_name = "buyer/dashboard.html"
    context ={}
    return render(request, template_name, context)


@login_required
@seller_required
def seller_dashboard(request):
    template_name = "seller/dashboard.html"
    context={'user':request.user}
    return render(request, template_name, context)

