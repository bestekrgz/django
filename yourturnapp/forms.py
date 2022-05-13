from django.forms import ModelForm
from django import forms
from .models import *


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'project_image', 'description', 'demo_link', 'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),

        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update({'class': 'input100'})
        # self.fields['description'].widget.attrs.update({'class': 'input100'})
        # self.fields['demo_link'].widget.attrs.update({'class': 'input100'})
        # self.fields['source_link'].widget.attrs.update({'class': 'input100'})
        # self.fields['project_image'].widget.attrs.update({'class': 'input100'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'comment']

    labels = {
        'value': 'Place your rating here',
        'comment': 'Place your comment here'
    }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})