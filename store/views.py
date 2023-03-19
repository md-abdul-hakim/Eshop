from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView

from store.models import Category, Product, ProductImages, Banner, Review
from store.forms import ReviewForm
from other.models import FAQ

class HomeListView(TemplateView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all().order_by('-id')
        top_products = Product.objects.filter(is_stock=True)[0:3]
        banners = Banner.objects.filter(is_active=True).order_by('-id')[0:3]
        context = {
            'products': products,
            'banners': banners,
            'top_products': top_products
        }
        return render(request, 'store/index.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            search_product = request.POST.get('search_product')
            products = Product.objects.filter(name__icontains=search_product).order_by('-id')
            context = {
                'products': products
            }
            return render(request, 'store/index.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_images'] = ProductImages.objects.filter(product=self.object.id)
        context['products'] = Product.objects.all().order_by('-id')
        context['reviews'] = Review.objects.filter(product=self.object.id).order_by('-id')
        context['total_review'] = Review.objects.filter(product=self.object.id).count()
        return context

def add_review(request, pk):
    if request.method == 'post' or request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rev = Review()
            rev.product = Product.objects.get(pk=pk)
            rev.user = request.user
            rev.subject = form.cleaned_data['subject']
            rev.description = form.cleaned_data['description']
            rev.review_number = form.cleaned_data['review_number']
            rev.save()
            return redirect('store:index')
    else:
        form = ReviewForm()
    context = {
        'form':form
    }
    return render(request, 'store/review-form.html', context)

def faq_view(request):
    payments = FAQ.objects.filter(active=True, category='payment')
    shippings = FAQ.objects.filter(active=True)
    order_returns = FAQ.objects.filter(active=True, Category='order_and_return')
    context = {
        'payments':payments,
        'shippings':shippings,
        'order_returns':order_returns
    }
    return render(request, 'faq.html', context)


    # item.get_product_url
# def product_details(request, pk):
#     item = Product.objects.get(id=pk)
#     photos = ProductImages.objects.filter(product=item).order_by('-created')
#     context = {
#         'item': item,
#         'photos': photos,
#     }
#     return render(request, 'store/product.html', context)