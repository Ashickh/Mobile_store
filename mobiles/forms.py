from django import forms



class MobileForm(forms.Form):
    mob_id=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-pill'}))
    mob_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-pill'}))
    brand = forms.CharField (widget=forms.TextInput (attrs={'class': 'form-control rounded-pill'}))
    price = forms.IntegerField (widget=forms.NumberInput (attrs={'class': 'form-control rounded-pill'}))
    color = forms.CharField (widget=forms.TextInput (attrs={'class': 'form-control rounded-pill'}))
    memory = forms.CharField (widget=forms.TextInput (attrs={'class': 'form-control rounded-pill'}))
