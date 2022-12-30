
from django import forms
from .models import Product, Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('product_name', 'product_number', 'text', 'price', 'is_in_stock', 'size', 'rating', 'product_image',)
        
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ( "item", "first_name", "last_name", "phone_number", "email", "country", "postal_code", "city", "street", "house_number", "payment", "delivery", "comment")