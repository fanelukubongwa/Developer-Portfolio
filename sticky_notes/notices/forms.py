from django import forms
from .models import Notice


class NoticeForm(forms.ModelForm):
    """
    Form for creating and updating Notice objects:

    Fields:
    -title: Charfield for the title.
    -content: Textfield for the notice content.

    Meta class:
    -Defines the model to use (Notice) and the fields to include in
    the form

    :param forms.ModelForm: Django's ModelForm class
    """

    class Meta:
        model = Notice
        fields = ["title", "content", "author"]
