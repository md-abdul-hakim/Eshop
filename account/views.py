from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm

from django.contrib.auth import get_user_model
User = get_user_model()

from account.models import Profile
from order.models import Cart, Order
from payment.models import BillingAddress
from payment.forms import BillingAddressForm
from account.forms import RegistrationForm, ProfileForm


def register(request):
    if request.user.is_authenticated:
        return HttpResponse('You are authenticated!')
    else:
        if request.method == 'post' or request.method == 'POST':
            # form = RegistrationForm(request.POST)
            # if form.is_valid():
            username = str(request.POST['username'])
            email = str(request.POST['email'])
            password = request.POST['password']
            reg = User(username=username, email=email, password=password)
            reg.is_active = True
            reg.save()
            return HttpResponse('Your Account has been created!')
        else:        
            form = RegistrationForm()        
        context = {
            'form': form
        }
    return render(request, 'login.html', context)

def Customerlogin(request):
    if request.user.is_authenticated:
        return HttpResponse('You are logged in!')
    else:
        if request.method == 'POST' or request.method == 'post':
            username = request.POST.get('username')
            password = request.POST.get('password')
            customer = authenticate(request, username=username, password=password)
            if customer is not None:
                login(request, customer)
                return redirect('store:index')
            else:
                return HttpResponse('404')
    return render(request, 'login.html')
def Customerlogout(request):
    logout(request)
    return render(request, 'login.html')

class ProfileView(TemplateView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(user=request.user, ordered=True)
        billingaddress = BillingAddress.objects.get(user=request.user)
        billingaddress_form = BillingAddressForm(instance=billingaddress)
        profile_obj = Profile.objects.get(user=request.user)
        profileForm = ProfileForm(instance=profile_obj)

        context = {
            'orders': orders,
            'billingaddress': billingaddress_form,
            'profileForm':profileForm,
        }
        return render(request, 'profile.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            billingaddress = BillingAddress.objects.get(user=request.user)
            billingaddress_form = BillingAddressForm(request.POST, instance=billingaddress)
            profile_obj = Profile.objects.get(user=request.user)
            profileForm = ProfileForm(request.POST, instance=profile_obj)
            if billingaddress_form.is_valid() or profileForm.is_valid():
                billingaddress_form.save()
                profileForm.save()
                return redirect('account:profile')
            
def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            update_session_auth_hash(request,form.user)
            messages.success(request,'password changed succesfully')
            return redirect('store:index')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'change_password.html',{'form':form})

# def activate(request,uidb64,token):
#     try:
#         uid=urlsafe_base64_decode(uidb64).decode()
#         user=UserModel._default_manager.get(pk=uid)
#     except(TypeError,ValueError,OverflowError,User.DoesNotExist):
#         user=None
#     if user is not None and  default_token_generator.check_token(user,token):
#         user.is_active=True
#         user.save()
#         messages.success(request,'Your account is activated,now you can login.')
#         return redirect('login')
#     else:
#         messages.warning(request,'activation link is invalid')
#         return redirect('signup')