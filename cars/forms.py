# similar like models.py
from django import forms
from .models import Review
from django.forms import ModelForm


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        # fields = ['first_name', 'last_name', 'stars']
        fields = "__all__" #same as like previous line

        labels = {
            'first_name': "YOUR FIRST NAME",
            'last_name': "YOUR LAST NAME",
            'stars': "Rating"
        }
        error_messages = {
            'stars':{
                'min_value':"Min Value is 1",
                'max_value':"Max Value is 5"
            }
        }