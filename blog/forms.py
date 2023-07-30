from django.forms import ModelForm

from .models import *

class BlogCreateForm(ModelForm):
    
    class Meta:
        model = Blog
        fields =[
            "title",
            "body",
            "image",
        ]