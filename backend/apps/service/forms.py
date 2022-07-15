from django import forms

from .models import  URL


class URLAddForm(forms.ModelForm):

    class Meta:
        model = URL
        fields = (
            'url',
            'check_interval'
        )
        widgets = {
            "url":forms.URLInput(attrs={"class":"form-control"}),
            "check_interval":forms.Select(attrs={"class":"form-control"})
        }