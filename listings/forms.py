from django.forms import ModelForm
from .models import Listing

class ListingForm(ModelForm):
    
    class Meta:
        model = Listing
        fields =["title","price",
        "no_bedroom","no_bathroom",
        "square_photage",
        "address","image"]


