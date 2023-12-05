from django import forms
from .models import Property, Unit, Tenant, RentalInformation

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'address', 'location', 'features']

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['rent_cost', 'unit_type']


class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'address', 'document_proofs']

class RentalInformationForm(forms.ModelForm):
    class Meta:
        model = RentalInformation
        fields = ['unit','agreement_end_date','monthly_rent_date']
        widgets = {
            'agreement_end_date': forms.DateInput(attrs={'type': 'date'}),
            'monthly_rent_date': forms.TextInput(attrs={'type': 'number'}),
        }
