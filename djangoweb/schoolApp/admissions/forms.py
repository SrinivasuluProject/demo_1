from  django import forms
from admissions.models import students


class studentsModelForm(forms.ModelForm):
    class Meta:
        model = students
        fields = '__all__'

class VendorForm(forms.Form):
    name=forms.CharField()
    address=forms.CharField()
    contact=forms.CharField()
    item=forms.CharField()
