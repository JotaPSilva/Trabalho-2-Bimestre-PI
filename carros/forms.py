from django import forms

from .models import Carro, MarcaCarro


class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = "__all__"
        widgets = {
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "ano": forms.NumberInput(attrs={"class": "form-control"}),
            "preco": forms.NumberInput(attrs={"class": "form-control"}),
            "marca": forms.Select(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control"}),
            "foto": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


class MarcaCarroForm(forms.ModelForm):
    class Meta:
        model = MarcaCarro
        fields = "__all__"
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
        }
