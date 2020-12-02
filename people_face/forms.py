from django import forms

class ImageForm(forms.Form):
    image1=forms.ImageField(widget=forms.FileInput())
    image2=forms.ImageField(widget=forms.FileInput())
    