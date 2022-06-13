from django import forms



class MobileForm(forms.Form):
    mob_id=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-pill'}))
    mob_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-pill'}))
    brand = forms.CharField (widget=forms.TextInput (attrs={'class': 'form-control rounded-pill'}))
    price = forms.IntegerField (widget=forms.NumberInput (attrs={'class': 'form-control rounded-pill'}))
    color = forms.CharField (widget=forms.TextInput (attrs={'class': 'form-control rounded-pill'}))
    memory = forms.IntegerField (widget=forms.NumberInput (attrs={'class': 'form-control rounded-pill'}))
    def clean(self):
        cleaned_data=super().clean()
        mry=cleaned_data.get("memory")
        pr=cleaned_data.get("price")
        if mry%2!=0:
            msg="Invalid Memory"
            self.add_error("memory",msg)
        elif pr<0:
            msg="Invalid Price"
            self.add_error("price",msg)
