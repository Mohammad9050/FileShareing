from django import forms

from Home.models import PostModel


class fileForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.FileField(widget=forms.FileInput)
    desc = forms.CharField(widget=forms.Textarea, required=False)
