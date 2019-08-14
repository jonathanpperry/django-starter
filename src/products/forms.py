from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                "class": "new-class-name two",
                "id": "this-id",
                "rows": 10,
                "cols": 150
            }))
    price = forms.DecimalField()
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your description"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "id": "this-id",
                "rows": 10,
                "cols": 70
            }))
    price = forms.DecimalField()