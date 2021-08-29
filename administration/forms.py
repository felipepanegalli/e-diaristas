from django import forms
from .models import Service
from decimal import Decimal


class ServiceForm(forms.ModelForm):
    min_value = forms.CharField(widget=forms.TextInput(attrs={"class": "money"}))
    percentage = forms.CharField(widget=forms.TextInput(attrs={"class": "money"}))
    bedroom_hour_price = forms.CharField(
        widget=forms.TextInput(attrs={"class": "money"})
    )
    living_room_hour_price = forms.CharField(
        widget=forms.TextInput(attrs={"class": "money"})
    )
    bathroom_hour_price = forms.CharField(
        widget=forms.TextInput(attrs={"class": "money"})
    )
    kitchen_hour_price = forms.CharField(
        widget=forms.TextInput(attrs={"class": "money"})
    )
    yard_hour_price = forms.CharField(widget=forms.TextInput(attrs={"class": "money"}))
    others_hour_price = forms.CharField(
        widget=forms.TextInput(attrs={"class": "money"})
    )

    class Meta:
        model = Service
        fields = "__all__"

    def clean_min_value(self):
        data = self.cleaned_data["min_value"]
        return Decimal(data.replace(",", "."))

    def clean_percentage(self):
        data = self.cleaned_data["percentage"]
        return Decimal(data.replace(",", "."))

    def clean_bedroom_hour_price(self):
        data = self.cleaned_data["bedroom_hour_price"]
        return Decimal(data.replace(",", "."))

    def clean_living_room_hour_price(self):
        data = self.cleaned_data["living_room_hour_price"]
        return Decimal(data.replace(",", "."))

    def clean_bathroom_hour_price(self):
        data = self.cleaned_data["bathroom_hour_price"]
        return Decimal(data.replace(",", "."))

    def clean_kitchen_hour_price(self):
        data = self.cleaned_data["kitchen_hour_price"]
        return Decimal(data.replace(",", "."))

    def clean_yard_hour_price(self):
        data = self.cleaned_data["yard_hour_price"]
        return Decimal(data.replace(",", "."))

    def clean_others_hour_price(self):
        data = self.cleaned_data["others_hour_price"]
        return Decimal(data.replace(",", "."))
