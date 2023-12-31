from django import forms


class MetaPostFileChecker(forms.Form):
    image = forms.ImageField()
    file = forms.FileField()
