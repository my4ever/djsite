from django import forms
from .models import Category, Women


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Имя')
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Биография')
    is_published = forms.BooleanField(required=False, initial=True, label='Опубкованно')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана')
