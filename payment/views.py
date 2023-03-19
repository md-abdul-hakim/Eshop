import json
from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

#models
from order.models import Cart, Order, OrderUpdate
from payment.models import BillingAddress
from payment.forms import BillingAddressForm, PaymentMethodForm

class CheckoutTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        saved_address = BillingAddress.objects.get_or_create(user=request.user or None)
        saved_address = saved_address[0]
        form = BillingAddressForm(instance=saved_address)
        payment_method = PaymentMethodForm()
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        order_item = order_qs[0].orderitems.all()
        order_total = order_qs[0].get_totals()
        pay_meth = request.GET.get('pay_meth')
        context = {
            'billing_address': form,
            'order_item': order_item,
            'order_total': order_total,
            'payment_method': payment_method,
            'paypal_client_id': settings.PAYPAL_CLIENT_ID,
            'pay_meth': pay_meth
        }
        return render(request, 'store/checkout.html', context)

    def post(self, request, *args, **kwargs):
        saved_address = BillingAddress.objects.get_or_create(user=request.user or None)
        saved_address = saved_address[0]
        form = BillingAddressForm(instance=saved_address)
        payment_obj = Order.objects.filter(user=request.user, ordered=False)[0]
        payment_form = PaymentMethodForm(instance=payment_obj)
        if request.method == 'post' or request.method == 'POST':
            form = BillingAddressForm(request.POST, instance=saved_address)
            pay_form = PaymentMethodForm(request.POST, instance=payment_obj)
            if form.is_valid() and pay_form.is_valid():
                form.save()
                pay_method = pay_form.save()               
                if not saved_address.is_fully_filled():
                    return redirect('checkout')
                
                # Cash on delivery payment proccess 
                if pay_method.payment_method == 'Cash on Delivery':
                    order_qs = Order.objects.filter(user=request.user, ordered=False)
                    order = order_qs[0]
                    order.ordered = True
                    order.orderId = order.id
                    order.paymentId = pay_method.payment_method
                    order.save()
                    order_update = OrderUpdate(order_id=order.orderId, update_desc="The order has been places!")
                    order_update.save()
                    cart_items = Cart.objects.filter(user=request.user, purchased=False)
                    for item in cart_items:
                        item.purchased = True
                        item.save()
                    print('Order Submited Successsfully')
                    return redirect('store:index')
                
                # paypal payment proccess
                if pay_method.payment_method == 'PayPal':
                    return redirect(reverse('checkout') + "?pay_meth=" + str(pay_method.payment_method))
                return redirect('checkout')

def paypalPaymentMethod(request):
    data = json.loads(request.body)
    order_id = data['order_id']
    payment_id = data['payment_id']
    status = data['status']

    if status == "COMPLETED":
        if request.user.is_authenticated:
            order_qs = Order.objects.filter(user=request.user, ordered=False)
            order = order_qs[0]
            order.ordered = True
            order.orderId = order_id
            order.paymentId = payment_id
            order.save()
            cart_items = Cart.objects.filter(user=request.user, purchased=False)
            for item in cart_items:
                item.purchased = True
                item.save()
    return redirect('store:index')