from django.shortcuts import render
from other.forms import UserContactForm
from other.models import UserContact, SiteContact, FAQ, AboutEshop
from store.models import Brand, Review

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def userContact(request):
    data = SiteContact.objects.all()
    if request.method == 'post' or request.method == 'POST':
        form = UserContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserContactForm()

    context = {
        'form':form,
        'data':data
    }
    return render(request, 'contact.html', context)

def faq_view(request):
    payments = FAQ.objects.filter(status=True, category='payment').order_by('created_at')
    shippings = FAQ.objects.filter(status=True, category='shipping').order_by('created_at')
    order_returns = FAQ.objects.filter(status=True, category='order_and_return').order_by('created_at')
    context = {
        'payments':payments,
        'shippings':shippings,
        'order_returns':order_returns
    }
    return render(request, 'faq.html', context)

def about_eshop(request):
    about = AboutEshop.objects.all().last()
    brands = Brand.objects.all()
    reviews = Review.objects.all()
    staffs = User.objects.filter(is_staff = True).order_by('id')
    context = {
        'about': about,
        'brands': brands,
        'reviews': reviews,
        'staffs': staffs
    }
    return render(request, 'about.html', context)