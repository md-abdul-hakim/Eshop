from django import forms
from order.models import Order
from payment.models import BillingAddress


class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ('__all__')
        exclude = ('user',)

class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method',]