from tkinter import Widget
from turtle import title
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'slug', 'author', 'content', 'status')
		Widget = {
			 'title': forms.TextInput(attrs={'class': 'form-control',}),
			 'slug': forms.TextInput(attrs={'class': 'form-control'}),
			 'author': forms.Select(attrs={'class': 'form-control'}),
			 'content': forms.Textarea(attrs={'class': 'form-control'}),
			 'status': forms.Select(attrs={'class': 'form-control'}),
		 }


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
















