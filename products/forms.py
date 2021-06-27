from django import forms
from .models import *

class FormProduct(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            "product_name",
            "product_description",
            "product_category",
            "product_price",
            "product_stock",
            "product_media"
        ]

        widgets = {
            "product_name" : forms.TextInput(attrs = {
                'class' : 'form-control font-control-sm',
                'placeholder' : 'Product Name..'
            }),
            "product_description" : forms.Textarea(attrs = {
                'class' : 'form-control form-control-sm',
                'placeholder' : 'Product Description ...'
            }),
            "product_price" : forms.NumberInput(attrs = {
                'class' : 'form-control form-control-sm',
                'placeholder' : 'Product Price..'
            }),
            "product_stock" : forms.NumberInput(attrs = {
                'class' : 'form-control form-control-sm',
                'placeholder' : 'Product Stock...'
            }),
            "product_media" : forms.FileInput(attrs={
                "class" : "form-control form-control-sm",
                "multiple" : True
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.values()
        catInputs = [[cat["id"], cat["name"]] for cat in categories]

        self.fields['product_category'] = forms.ChoiceField(choices = catInputs)
        self.fields['product_category'].widget.attrs.update({'class': 'form-control form-control-sm'})

        

class FormCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "name",
            "description"
        ]

        widgets = {
            "name" : forms.TextInput(attrs = {
                "class" : "form-control form-control-sm",
                "placeholder" : "Category Name..."
            }),
            "description" : forms.Textarea(attrs = {
                "class" : "form-control form-control-sm",
                "placeholder" : "Category Description..."
            })
        }

class FormRating(forms.ModelForm):
    class Meta:
        model = Rating
        fields = [
            "comments",
            "rate"
        ]

        widgets = {
            "comments" : forms.Textarea(attrs = {
                "class" : "form-control form-control-sm",
                "placeholder" : "Comments"
            }),
            "rate" : forms.NumberInput(attrs = {
                "class" : "form-control form-control-sm",
                "placeholder" : "Rate 1-5..."
            })
        }

class FormDiscount(forms.ModelForm):
    class Meta:
        model = Discount
        fields = [
            "name",
            "description",
            "discount"
        ]

        widgets = {
            "name" : forms.TextInput(attrs = {
                "class" : "form-control form-control-sm",
                "placeholder" : "Discount Name..."
            }),
            "description" : forms.Textarea(attrs = {
                "class" : "form-control form-control-sm",
                "placeholder" : "Discount Description..."
            }),
            "discount" : forms.NumberInput(attrs = {
                "class" : "form-control form-control-sm",
                "placeholder" : "Discount Percent..."
            })
        }