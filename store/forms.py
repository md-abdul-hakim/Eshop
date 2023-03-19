from django import forms
from store.models import Category,  Product,  VariationValue,  Banner,  MyLogo,  MyFavicon, Review

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')
        exclude = ['slug']
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('__all__')
        exclude = ['user', 'product', 'created_at']