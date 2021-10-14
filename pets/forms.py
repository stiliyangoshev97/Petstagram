from django.forms import ModelForm
from django import forms

from pets.models import Pet, Comment, Like

class PetForm(ModelForm):
    class Meta:
        model = Pet
        exclude = ('user',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'pet_form'})
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ('user', 'pet',)
        widgets = {
            'text': forms.Textarea(attrs={'class': 'comment_form'})
        }


class LikeForm(ModelForm):
    class Meta:
        model = Like
        exclude = ('pet', 'user',)