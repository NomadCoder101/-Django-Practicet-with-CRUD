from django.forms import ModelForm

from .models import *
    
class CreateForm(ModelForm):
       
    class Meta:
        model = Listing
        fields = [
                   "title",
                   "price",
                   "num_bedrooms",
                   "num_bathrooms",
                   "square_footage",
                   "address",
                   "image",
                     
        ]
   