from django import forms
from .models import Card, Category

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['question', 'answer', 'category']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'parent']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например: Программирование'}),
            'parent': forms.Select(attrs={'class': 'form-select'}),
        }