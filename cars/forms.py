from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'title', 'color', 'model', 'year', 'price', 'body_style',
            'engine', 'transmission', 'interior', 'mileage', 'features',
            'description', 'car_photo', 'car_photo_1', 'car_photo_2',
            'car_photo_3', 'car_photo_4', 'is_featured'
        ]
