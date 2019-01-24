from django.forms import ModelForm
from .models import Post
from django import forms

class TweetForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']

    def __init__(self, *args, **kwargs):
        super(TweetForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'rows':2,
            'name': '',
            'placeholder': 'Tweet header'})
        self.fields['text'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter tweet'})
