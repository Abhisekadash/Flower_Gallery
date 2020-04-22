from django import forms
from .models import Picture_model

class ImageForm(forms.ModelForm):
	class Meta:
		model = Picture_model
		fields = ('name','image',)