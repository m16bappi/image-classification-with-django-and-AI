from django import forms


class imageUploadForm(forms.Form):
    image = forms.ImageField()
