from django import forms
from .models import checkout

class checkoutForm(forms.ModelForm):
    class Meta:
        model=checkout
        fields=['name','email','address','paymenttype']
